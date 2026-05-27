# Visa Sponsorship Atlas

> AI-powered directory of visa-sponsored job sites across 20+ countries. Microservices architecture, full-stack, zero-install database.

**Stack:** FastAPI · Next.js 14 · SQLite · Framer Motion · Docker Compose

---

## What it does

- Browse curated lists of job sites per country
- Filter by: government portals, free for candidates, entry-level friendly
- AI-powered matching: paste your skills → get top 5 country recommendations
- 20 countries seeded with **70 real, verified URLs** (mix of official government portals + free recruiters + job boards)

## Architecture

```
┌──────────┐      ┌────────────┐      ┌──────────────┐
│ Frontend │─────▶│  Gateway   │─────▶│ Jobs Service │
│ Next.js  │      │  FastAPI   │      │  (SQLite)    │
│  :3000   │      │   :8000    │      │    :8001     │
└──────────┘      │            │      └──────────────┘
                  │            │      ┌──────────────┐
                  │            │─────▶│  AI Service  │
                  │            │      │  (Claude)    │
                  └────────────┘      │    :8002     │
                                      └──────────────┘
```

3 backend microservices, 1 Next.js frontend, all containerised.

## Quick start

```bash
git clone <your-repo>
cd visa-jobs-platform

# Optional: add ANTHROPIC_API_KEY for real AI matching
cp .env.example .env

docker compose up --build
```

Open http://localhost:3000

That's it. SQLite gets seeded automatically on first run with all 20 countries + 70 sites.

## Run without Docker (dev mode)

You need Python 3.10+ and Node 18+.

```bash
# Terminal 1: Jobs Service
cd services/jobs-service
pip install -r requirements.txt
python seed.py
uvicorn main:app --port 8001

# Terminal 2: AI Service
cd services/ai-service
pip install -r requirements.txt
JOBS_SERVICE_URL=http://localhost:8001 uvicorn main:app --port 8002

# Terminal 3: Gateway
cd services/gateway
pip install -r requirements.txt
JOBS_SERVICE_URL=http://localhost:8001 AI_SERVICE_URL=http://localhost:8002 \
  uvicorn main:app --port 8000

# Terminal 4: Frontend
cd frontend
npm install
npm run dev
```

## API Endpoints

All routes via gateway at `http://localhost:8000`:

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/countries` | List all countries |
| GET | `/api/countries/:slug` | Country detail + job sites |
| GET | `/api/job-sites?is_government=true` | Filter sites globally |
| GET | `/api/stats` | Quick counts |
| POST | `/api/ai/match` | AI-recommend countries from skills text |

## Project structure

```
visa-jobs-platform/
├── docker-compose.yml
├── .env.example
│
├── frontend/                  # Next.js 14, App Router
│   ├── app/                   # Pages
│   ├── components/            # CountryCard, FadeIn
│   └── lib/                   # api.ts, types.ts
│
└── services/
    ├── gateway/               # API gateway, FastAPI proxy
    ├── jobs-service/          # SQLite + countries/jobs API
    │   ├── models.py          # SQLAlchemy ORM
    │   ├── schemas.py         # Pydantic
    │   ├── seed_data.py       # 20 countries, 70 verified URLs
    │   └── main.py
    └── ai-service/            # Claude-powered matching
```

## Why these choices

- **SQLite** — zero install, no Postgres server needed. Fine for 10-100 users.
- **3 microservices** — small enough to grok, large enough to demonstrate distributed-systems thinking.
- **AI fallback** — works without ANTHROPIC_API_KEY (keyword-based). With a key, uses Claude Haiku for smart matching.

## Data sources

Government portals were verified at time of writing. Things change — if a URL breaks, edit `services/jobs-service/seed_data.py` and re-run seed.

**Most reliable sources to apply through:**
- Government portals (🏛️) — `make-it-in-germany.com`, `jobbank.gc.ca`, `mycareersfuture.gov.sg`, etc.
- Tech-focused free recruiters (🆓) — VanHack, Honeypot, Landing.jobs, Relocate.me
- Visa-sponsor employer lists — UK Sponsor License Register, NL IND Recognized Sponsors

## Deploying

For a CV-worthy deploy, options:

1. **Hetzner / DigitalOcean VPS ($5-10/mo)** — `docker compose up -d` and point a domain. Easiest.
2. **Railway / Render** — one-click deploy per service.
3. **Fly.io** — global edge, free tier. Great line on a CV.
4. **Kubernetes** — overkill for traffic, but resume gold. Use the docker-compose as a starting point.

## License

MIT.
