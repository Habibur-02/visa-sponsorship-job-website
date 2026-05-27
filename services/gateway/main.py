"""
API Gateway. Single entry point for the frontend.
Forwards to internal services. Handles CORS + logging.
"""
import os
import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

JOBS_URL = os.getenv("JOBS_SERVICE_URL", "http://jobs-service:8001")
AI_URL = os.getenv("AI_SERVICE_URL", "http://ai-service:8002")

app = FastAPI(title="API Gateway", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def proxy(request: Request, base_url: str, path: str):
    """Forward request to internal service, return its response."""
    url = f"{base_url}{path}"
    method = request.method
    body = await request.body()
    headers = {k: v for k, v in request.headers.items() if k.lower() != "host"}
    params = dict(request.query_params)

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            resp = await client.request(
                method, url, content=body, headers=headers, params=params
            )
        except httpx.RequestError as e:
            raise HTTPException(502, f"Upstream error: {e}")

    return JSONResponse(
        content=resp.json() if resp.content else None,
        status_code=resp.status_code,
    )


@app.get("/health")
def health():
    return {"status": "ok", "service": "gateway"}


# Jobs service routes
@app.api_route("/api/countries{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def jobs_countries(request: Request, path: str):
    return await proxy(request, JOBS_URL, f"/countries{path}")


@app.api_route("/api/job-sites{path:path}", methods=["GET"])
async def jobs_sites(request: Request, path: str):
    return await proxy(request, JOBS_URL, f"/job-sites{path}")


@app.get("/api/stats")
async def jobs_stats(request: Request):
    return await proxy(request, JOBS_URL, "/stats")


# AI service routes
@app.api_route("/api/ai/{path:path}", methods=["GET", "POST"])
async def ai_proxy(request: Request, path: str):
    return await proxy(request, AI_URL, f"/{path}")
