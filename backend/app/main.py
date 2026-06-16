"""
main.py

This is the entry point of the FastAPI application.

Responsibilities:
1. Create FastAPI application
2. Enable CORS
3. Register API routes
4. Provide health check endpoint
"""

# FastAPI core framework
from fastapi import FastAPI

# Middleware used for CORS
from fastapi.middleware.cors import CORSMiddleware

# Import resume routes
from app.routes.resume import router as resume_router


# ----------------------------------------------------
# Create FastAPI Application
# ----------------------------------------------------
# This creates the backend server instance.
# Everything in FastAPI starts from here.
# ----------------------------------------------------

app = FastAPI(
    title="AI Resume Reviewer API",
    description="Backend API for Resume Review using Llama3 and Ollama",
    version="1.0.0"
)


# ----------------------------------------------------
# Enable CORS
# ----------------------------------------------------
# Why?
#
# React frontend runs on:
# http://localhost:5173
#
# FastAPI backend runs on:
# http://localhost:8000
#
# Browser treats them as different origins.
#
# Without CORS:
# Access blocked by browser.
#
# With CORS:
# React can call FastAPI APIs.
# ----------------------------------------------------

app.add_middleware(
    CORSMiddleware,

    # Allow frontend URL
    allow_origins=[
        "http://localhost:5173"
    ],

    # Allow cookies/auth headers if needed later
    allow_credentials=True,

    # Allow all HTTP methods
    allow_methods=["*"],

    # Allow all request headers
    allow_headers=["*"],
)


# ----------------------------------------------------
# Register Routes
# ----------------------------------------------------
# All resume related APIs will start with:
#
# /api/resume
#
# Example:
#
# POST /api/resume/review
#
# ----------------------------------------------------

app.include_router(
    resume_router,
    prefix="/api/resume",
    tags=["Resume Reviewer"]
)


# ----------------------------------------------------
# Root Endpoint
# ----------------------------------------------------
# Health check endpoint.
#
# Useful for:
# - Testing API
# - Deployment validation
# - Monitoring
# ----------------------------------------------------

@app.get("/")
def health_check():
    """
    Simple API health check.
    """

    return {
        "success": True,
        "message": "AI Resume Reviewer API is running"
    }


# ----------------------------------------------------
# Optional Version Endpoint
# ----------------------------------------------------
# Useful in production.
# Helps frontend know which backend version
# is currently deployed.
# ----------------------------------------------------

@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }