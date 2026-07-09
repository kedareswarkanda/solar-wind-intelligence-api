# Solar & Wind Deployment Intelligence Platform - FastAPI Backend

## 1. Project Overview
This repository contains the initial FastAPI backend setup for the Solar & Wind Deployment Intelligence Platform. The platform is associated with renewable energy deployment intelligence. This implementation focuses on local FastAPI setup and basic API endpoints.

## 2. Internship Assignment
This project fulfills the requirements of the **Infosys Springboard Virtual Internship 7.0**:
*   Task 1 - Successfully run FastAPI locally.
*   Task 2 - Create GET /about and GET /health endpoints.

## 3. Day 2 - Modular Router Architecture
As part of the Day 2 assignment, the application has been refactored into a modular design:
*   The root endpoint (`GET /`) was refactored and moved from `main.py` to a dedicated home router: `app/api/home.py`.
*   Feature routers were created for projects (`app/api/projects.py`), sites (`app/api/sites.py`), and predictions (`app/api/predictions.py`).
*   All four routers were registered with the FastAPI application using `app.include_router()`.
*   `GET /projects` was implemented to return a hardcoded list of available renewable energy projects.
*   `GET /sites` was implemented to return hardcoded renewable energy site coordinates.
*   The predictions router (`app/api/predictions.py`) was registered with the app but remains empty, ready to receive future prediction logic.

## 4. Day 3 - SQLAlchemy and PostgreSQL Persistence Layer Setup
As part of the Day 3 assignment, database configuration and ORM mapping have been established:
*   **SQLAlchemy Configuration**: Created a database configuration layer under `app/database/database.py` initializing:
    *   `engine`: Connects SQLAlchemy with the local PostgreSQL server.
    *   `SessionLocal`: Factory for creating individual database sessions.
    *   `Base`: Parent declarative base class for mapping Python model classes to database tables.
*   **Database Integration**: Configured database connection using the environment variable `DATABASE_URL` stored safely in a local `.env` file (ignored by Git for security).
*   **Project ORM Model**: Created the database model under `app/models/project.py` mapping to the PostgreSQL `projects` table:
    *   `id`: Integer, Primary Key.
    *   `project_name`: String.
    *   `location`: String.
*   **Automatic Table Generation**: Imported `Base`, `engine`, and the `Project` model inside `main.py`, executing `Base.metadata.create_all(bind=engine)` upon application startup to automatically create the `projects` table in PostgreSQL.
*   **API and Model Alignment**: Verified that the Project SQLAlchemy model and the fields in `GET /projects` represent the same entity exactly (`id`, `project_name`, `location`).
*   *Note: According to internship requirements, `GET /projects` still returns hardcoded data and is not yet connected to read from the PostgreSQL database. The persistence layer has been prepared for future database integration.*

## 5. Features
*   FastAPI backend setup with modular router architecture
*   Local Uvicorn server
*   SQLAlchemy ORM integration with PostgreSQL
*   Automatic database table creation
*   `GET /` endpoint (Home welcome route)
*   `GET /projects` endpoint (Renewable projects list - hardcoded)
*   `GET /sites` endpoint (Renewable site coordinates - hardcoded)
*   `GET /health` endpoint (System status regression check)
*   `GET /about` endpoint (Project information regression check)
*   JSON API responses
*   Swagger UI documentation

## 6. Project Structure
The repository contains the following clean, professional project structure:
```text
solar-wind-intelligence-api/
│
├── main.py
│
├── app/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── home.py
│   │   ├── projects.py
│   │   ├── sites.py
│   │   └── predictions.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   └── models/
│       ├── __init__.py
│       └── project.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```
*Note: The virtual environment (`venv/`) and environment variable configuration (`.env`) are kept locally and ignored from the Git repository using `.gitignore`.*

## 7. Prerequisites
To run this application, make sure you have the following installed on your system:
*   **Python 3.8+** (Ensure Python is added to your system's PATH variable)
*   **pip** (Python package installer, which comes bundled with Python)
*   **PostgreSQL** database installed and running locally
*   **VS Code** (Recommended IDE for a smooth development experience)

## 8. Installation
Follow these Windows-friendly commands to set up the project on your local system:

### Step 1: Clone and Navigate to the Project Folder
Clone the repository and navigate into the project directory:
```bash
git clone <repository-url>
cd solar-wind-intelligence-api
```
Alternatively, open VS Code, select **File > Open Folder**, and choose the `solar-wind-intelligence-api` directory.

### Step 2: Create a Virtual Environment
Create a local virtual environment named `venv` inside the project folder:
*   In PowerShell or Command Prompt:
    ```bash
    python -m venv venv
    ```
    *(If the command above does not work, try: `py -m venv venv`)*

### Step 3: Activate the Virtual Environment
Activate the environment to isolate the project's dependencies:
*   **For Windows PowerShell:**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
*   **For Windows Command Prompt:**
    ```cmd
    venv\Scripts\activate
    ```

### Step 4: Install Dependencies
Install all the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables
Create a `.env` file in the root folder of the project and add the database URL containing your PostgreSQL database credentials:
```text
DATABASE_URL=postgresql://postgres:YOUR_POSTGRES_PASSWORD@localhost:5432/solar_wind_db
```
*(Make sure to URL-encode any special characters in your password, e.g. replacing `@` with `%40`)*

## 9. Running the Application
Start the Uvicorn ASGI development server using the command below:
```bash
uvicorn main:app --reload
```

### Command Breakdown:
*   `uvicorn`: The ASGI server that runs the web application.
*   `main`: The Python file (`main.py`) containing the code.
*   `app`: The FastAPI application object initialized inside `main.py` (`app = FastAPI(...)`).
*   `--reload`: Automatically reloads the server whenever you save changes to your code.

## 10. Local Server URL
Once started, the local development server will be running at:
*   **Local Server Address:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 11. Swagger UI
FastAPI automatically generates interactive Swagger UI documentation at:
*   **Swagger UI Address:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 12. API Endpoints
The platform exposes the following GET endpoints:

### 1. Welcome Endpoint
*   **Route:** `GET /`
*   **Expected Response:**
    ```json
    {
      "message": "Welcome to Solar & Wind Deployment Intelligence Platform"
    }
    ```

### 2. Projects Endpoint
*   **Route:** `GET /projects`
*   **Expected Response:**
    ```json
    [
      {
        "id": 1,
        "project_name": "Demo Solar Project",
        "location": "Odisha"
      }
    ]
    ```

### 3. Sites Endpoint
*   **Route:** `GET /sites`
*   **Expected Response:**
    ```json
    [
      {
        "id": 1,
        "latitude": 19.8135,
        "longitude": 85.8312
      }
    ]
    ```

### 4. Health Check Endpoint
*   **Route:** `GET /health`
*   **Expected Response:**
    ```json
    {
      "status": "Running"
    }
    ```

### 5. About Endpoint
*   **Route:** `GET /about`
*   **Expected Response:**
    ```json
    {
      "project": "Solar & Wind Deployment Intelligence Platform"
    }
    ```

## 13. Swagger API Documentation
How to test using Swagger UI:
1. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your web browser.
2. Select any endpoint (e.g., `GET /projects` or `GET /sites`) to expand it.
3. Click the **Try it out** button in the top-right of the endpoint section.
4. Click the blue **Execute** button.
5. Scroll down to review the **Response body** showing the JSON output and verify the **Response headers** show a `200` status code.

## 14. API Testing
You can manually verify the API endpoints directly in your browser:
*   Accessing [http://127.0.0.1:8000/projects](http://127.0.0.1:8000/projects) should display the hardcoded list of projects.
*   Accessing [http://127.0.0.1:8000/sites](http://127.0.0.1:8000/sites) should display the coordinates.
*   Accessing [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) should display `{"status": "Running"}`.
*   Accessing [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about) should display the project name.

## 15. Assignment Result
The database and persistence configuration for Day 3 has been successfully completed, integrating SQLAlchemy Engine, SessionLocal, and declarative Base. The Project ORM database model maps correctly to the PostgreSQL projects table schema, generated automatically upon application startup. Both new API endpoints return the exact JSON values required, tested successfully on localhost.
