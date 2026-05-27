"""
Seed the SQLite database. Idempotent: deletes & re-inserts on each run.
Run: python seed.py
"""
from database import engine, SessionLocal, Base
from models import Country, JobSite
from seed_data import COUNTRIES_DATA


def seed():
    print("📦 Creating tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        for c in COUNTRIES_DATA:
            sites = c.pop("job_sites", [])
            country = Country(**c)
            db.add(country)
            db.flush()  # get country.id

            for s in sites:
                # Sensible defaults
                s.setdefault("hires_entry_level", True)
                s.setdefault("is_free", True)
                s.setdefault("pay_after_hire", False)
                db.add(JobSite(country_id=country.id, **s))

        db.commit()
        n_countries = db.query(Country).count()
        n_sites = db.query(JobSite).count()
        print(f"✅ Seeded {n_countries} countries, {n_sites} job sites.")
    except Exception as e:
        db.rollback()
        print(f"❌ Seed failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
