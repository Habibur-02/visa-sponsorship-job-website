"""
AI Service. Takes a user's skill/experience text, recommends best
matching countries + job sites using Claude.

Works WITHOUT an API key in 'demo mode' (keyword fallback).
With ANTHROPIC_API_KEY set, uses Claude for smart matching.
"""
import os
import json
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
JOBS_URL = os.getenv("JOBS_SERVICE_URL", "http://jobs-service:8001")

app = FastAPI(title="AI Service", version="1.0.0")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class MatchRequest(BaseModel):
    skills_text: str  # "I am a Python backend dev with 2 yrs exp..."
    target_continent: Optional[str] = None
    entry_level_only: bool = True


class MatchResponse(BaseModel):
    recommended_countries: List[dict]
    advice: str
    used_llm: bool


@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-service", "llm_enabled": bool(ANTHROPIC_API_KEY)}


async def fetch_countries():
    """Pull all countries from jobs-service."""
    async with httpx.AsyncClient(timeout=10.0) as c:
        r = await c.get(f"{JOBS_URL}/countries")
        r.raise_for_status()
        return r.json()


async def call_claude(skills: str, countries: list) -> dict:
    """Use Claude to pick the best 5 countries."""
    countries_summary = "\n".join(
        f"- {c['name']} ({c['continent']}): {c['summary']}" for c in countries
    )
    prompt = f"""User profile:
{skills}

Available countries:
{countries_summary}

Pick the TOP 5 countries best suited for this user's visa-sponsored job search. Return JSON ONLY:
{{
  "picks": [
    {{"slug": "...", "reason": "1 sentence why"}}
  ],
  "advice": "2-3 sentences of practical advice"
}}"""

    async with httpx.AsyncClient(timeout=30.0) as c:
        r = await c.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": prompt}],
            },
        )
        r.raise_for_status()
        text = r.json()["content"][0]["text"]
        # Strip code fences if any
        text = text.strip().lstrip("```json").lstrip("```").rstrip("```").strip()
        return json.loads(text)


def keyword_fallback(skills: str, countries: list) -> dict:
    """No LLM available. Simple ranking by entry-friendliness."""
    s = skills.lower()
    is_tech = any(k in s for k in ["python", "java", "developer", "engineer", "tech", "data", "software"])
    picks = []
    for c in countries:
        score = 0
        if c["entry_friendly"]:
            score += 2
        if c["visa_difficulty"] <= 2:
            score += 2
        if is_tech and c["name"] in ("Germany", "Netherlands", "Ireland", "Portugal", "Estonia"):
            score += 3
        picks.append((score, c))
    picks.sort(key=lambda x: -x[0])
    top5 = picks[:5]
    return {
        "picks": [
            {"slug": c["slug"], "reason": f"Entry-friendly visa, {c['continent']}."}
            for _, c in top5
        ],
        "advice": "This is a keyword-based recommendation. For better matches, set ANTHROPIC_API_KEY to enable AI reasoning.",
    }


@app.post("/match", response_model=MatchResponse)
async def match(req: MatchRequest):
    countries = await fetch_countries()

    # Filter
    if req.target_continent:
        countries = [c for c in countries if c["continent"] == req.target_continent]
    if req.entry_level_only:
        countries = [c for c in countries if c["entry_friendly"]]

    if not countries:
        raise HTTPException(404, "No matching countries with given filters")

    used_llm = False
    try:
        if ANTHROPIC_API_KEY:
            result = await call_claude(req.skills_text, countries)
            used_llm = True
        else:
            result = keyword_fallback(req.skills_text, countries)
    except Exception as e:
        # Graceful fallback if LLM call fails
        result = keyword_fallback(req.skills_text, countries)
        result["advice"] += f" (LLM call failed: {e})"

    # Enrich picks with country details
    by_slug = {c["slug"]: c for c in countries}
    enriched = []
    for p in result["picks"]:
        c = by_slug.get(p["slug"])
        if c:
            enriched.append({**c, "reason": p["reason"]})

    return MatchResponse(
        recommended_countries=enriched,
        advice=result["advice"],
        used_llm=used_llm,
    )
