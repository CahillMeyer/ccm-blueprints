# /backend/app/main.py
from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

from .api.endpoints import time_zones
from .core.config import settings

# --- FastAPI App Setup ---
app = FastAPI(
    title="Micro-SaaS Starter API",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS Middleware (dev-only setting for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Routes ---
app.include_router(time_zones.router, prefix=settings.API_V1_STR)

# --- Health Check ---
@app.get("/")
def read_root():
    return {"message": "API is online and ready for deployment."}

# --- AWS Lambda Handler ---
# The handler Mangum uses to interface with AWS Lambda and API Gateway
handler = Mangum(app)
