"""Pydantic response schemas."""
from pydantic import BaseModel
from typing import List, Optional


class JobSiteOut(BaseModel):
    id: int
    name: str
    url: str
    description: Optional[str] = None
    site_type: Optional[str] = None
    is_government: bool
    hires_entry_level: bool
    is_free: bool
    pay_after_hire: bool
    rank: int
    notes: Optional[str] = None

    class Config:
        from_attributes = True


class CountryListOut(BaseModel):
    id: int
    name: str
    slug: str
    iso_code: str
    flag_emoji: Optional[str] = None
    continent: Optional[str] = None
    summary: Optional[str] = None
    visa_difficulty: int
    entry_friendly: bool
    job_site_count: int = 0

    class Config:
        from_attributes = True


class CountryDetailOut(BaseModel):
    id: int
    name: str
    slug: str
    iso_code: str
    flag_emoji: Optional[str] = None
    continent: Optional[str] = None
    summary: Optional[str] = None
    visa_difficulty: int
    entry_friendly: bool
    avg_salary_usd: Optional[int] = None
    currency: Optional[str] = None
    notes: Optional[str] = None
    job_sites: List[JobSiteOut] = []

    class Config:
        from_attributes = True
