from fastapi import FastAPI

# Initialize the FastAPI application with professional metadata
app = FastAPI(
    title="Solar & Wind Deployment Intelligence Platform API",
    description="Backend API for the Solar & Wind Deployment Intelligence Platform",
    version="1.0.0"
)


@app.get("/", tags=["General"])
def read_root():
    """
    Root endpoint that provides a welcoming message for the platform.
    """
    return {"message": "Welcome to Solar & Wind Deployment Intelligence Platform"}


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
