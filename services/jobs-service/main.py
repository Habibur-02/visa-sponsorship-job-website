"""Jobs Service — countries + job sites API."""
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from typing import List, Optional

from database import get_db, engine, Base
from models import Country, JobSite
from schemas import CountryListOut, CountryDetailOut, JobSiteOut

# Create tables if they don't exist (idempotent)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Jobs Service", version="1.0.0")

# CORS for local dev. Gateway will be the prod entry point.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok", "service": "jobs-service"}


@app.get("/countries", response_model=List[CountryListOut])
def list_countries(
    q: Optional[str] = Query(None, description="Search query"),
    continent: Optional[str] = None,
    entry_friendly: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    """List all countries with job site count."""
    query = db.query(
        Country,
        func.count(JobSite.id).label("site_count"),
    ).outerjoin(JobSite).group_by(Country.id)

    if q:
        like = f"%{q.lower()}%"
        query = query.filter(
            or_(
                func.lower(Country.name).like(like),
                func.lower(Country.summary).like(like),
            )
        )
    if continent:
        query = query.filter(Country.continent == continent)
    if entry_friendly is not None:
        query = query.filter(Country.entry_friendly == entry_friendly)

    rows = query.order_by(Country.name).all()
    out = []
    for country, count in rows:
        d = CountryListOut.model_validate(country).model_dump()
        d["job_site_count"] = count
        out.append(d)
    return out


@app.get("/countries/{slug}", response_model=CountryDetailOut)
def get_country(slug: str, db: Session = Depends(get_db)):
    """Get country with all its job sites, ordered by priority."""
    country = db.query(Country).filter(Country.slug == slug).first()
    if not country:
        raise HTTPException(404, detail="Country not found")

    # Sort sites: government first, then by rank
    country.job_sites.sort(key=lambda s: (not s.is_government, s.rank))
    return country


@app.get("/job-sites", response_model=List[JobSiteOut])
def list_job_sites(
    is_government: Optional[bool] = None,
    is_free: Optional[bool] = None,
    pay_after_hire: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    """Cross-country job site filter."""
    query = db.query(JobSite)
    if is_government is not None:
        query = query.filter(JobSite.is_government == is_government)
    if is_free is not None:
        query = query.filter(JobSite.is_free == is_free)
    if pay_after_hire is not None:
        query = query.filter(JobSite.pay_after_hire == pay_after_hire)
    return query.order_by(JobSite.rank).limit(100).all()


@app.get("/stats")
def stats(db: Session = Depends(get_db)):
    return {
        "countries": db.query(Country).count(),
        "job_sites": db.query(JobSite).count(),
        "government_sites": db.query(JobSite).filter(JobSite.is_government == True).count(),
    }
