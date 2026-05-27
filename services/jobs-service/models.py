"""SQLAlchemy ORM models."""
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, ForeignKey, DateTime, Float
)
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    iso_code = Column(String(3), unique=True, nullable=False)
    flag_emoji = Column(String(10))
    continent = Column(String(50))
    summary = Column(Text)
    visa_difficulty = Column(Integer, default=3)  # 1=easy, 5=hard
    entry_friendly = Column(Boolean, default=True)  # fresher/entry-level hiring
    avg_salary_usd = Column(Integer)
    currency = Column(String(10))
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    job_sites = relationship(
        "JobSite", back_populates="country", cascade="all, delete-orphan"
    )


class JobSite(Base):
    __tablename__ = "job_sites"

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
    name = Column(String(150), nullable=False)
    url = Column(Text, nullable=False)
    description = Column(Text)
    site_type = Column(String(30))  # 'government', 'free_agency', 'job_board', 'pay_after'
    is_government = Column(Boolean, default=False)
    hires_entry_level = Column(Boolean, default=True)
    is_free = Column(Boolean, default=True)
    pay_after_hire = Column(Boolean, default=False)
    rank = Column(Integer, default=99)  # smaller = higher priority
    notes = Column(Text)

    country = relationship("Country", back_populates="job_sites")
