from fastapi import FastAPI

from app.api.home import router as home_router
from app.api.projects import router as projects_router
from app.api.sites import router as sites_router
from app.api.predictions import router as predictions_router

# Initialize the FastAPI application with professional metadata
app = FastAPI(
    title="Solar & Wind Deployment Intelligence Platform API",
    description="Backend API for the Solar & Wind Deployment Intelligence Platform",
    version="1.0.0"
)

# Register feature routers
app.include_router(home_router)
app.include_router(projects_router)
app.include_router(sites_router)
app.include_router(predictions_router)


@app.get("/health", tags=["System"])
def health_check():
    """
    Health check endpoint to verify if the FastAPI backend is operational.
    """
    return {"status": "Running"}


@app.get("/about", tags=["Project"])
def about_project():
    """
    About endpoint to identify the project associated with this backend API.
    """
    return {"project": "Solar & Wind Deployment Intelligence Platform"}
