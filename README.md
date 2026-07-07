# Solar & Wind Deployment Intelligence Platform - FastAPI Backend

## 1. Project Overview
This repository contains the initial FastAPI backend setup for the Solar & Wind Deployment Intelligence Platform. The platform is associated with renewable energy deployment intelligence. This implementation focuses on local FastAPI setup and basic API endpoints.

## 2. Internship Assignment
This project fulfills the requirements of the **Infosys Springboard Virtual Internship 7.0**:
*   Task 1 - Successfully run FastAPI locally.
*   Task 2 - Create GET /about and GET /health endpoints.

## 3. Features
*   FastAPI backend setup
*   Local Uvicorn server
*   GET / endpoint
*   GET /health endpoint
*   GET /about endpoint
*   JSON API responses
*   Swagger UI documentation

## 4. Technologies Used
*   **Python**: Programming language used for development.
*   **FastAPI**: A modern, fast (high-performance), web framework for building APIs.
*   **Uvicorn**: A lightning-fast ASGI server implementation, used to run the FastAPI application.
*   **Swagger UI**: Automatically generated interactive API documentation.

## 5. Project Structure
The repository contains the following clean, professional project structure:
```text
solar-wind-intelligence-api/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```
*Note: The virtual environment (`venv/`) is kept locally and ignored from the Git repository using `.gitignore`.*

## 6. Prerequisites
To run this application, make sure you have the following installed on your system:
*   **Python 3.8+** (Ensure Python is added to your system's PATH variable)
*   **pip** (Python package installer, which comes bundled with Python)
*   **VS Code** (Recommended IDE for a smooth development experience)

## 7. Installation
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
    *(Note: If you get a script execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first, then run the activation script again).*
*   **For Windows Command Prompt:**
    ```cmd
    venv\Scripts\activate
    ```

### Step 4: Install Dependencies
Install all the required Python packages:
```bash
pip install -r requirements.txt
```

## 8. Running the Application
Start the Uvicorn ASGI development server using the command below:
```bash
uvicorn main:app --reload
```

### Command Breakdown:
*   `uvicorn`: The ASGI server that runs the web application.
*   `main`: The Python file (`main.py`) containing the code.
*   `app`: The FastAPI application object initialized inside `main.py` (`app = FastAPI(...)`).
*   `--reload`: Automatically reloads the server whenever you save changes to your code.

## 9. Local Server URL
Once started, the local development server will be running at:
*   **Local Server Address:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 10. Swagger UI
FastAPI automatically generates interactive Swagger UI documentation at:
*   **Swagger UI Address:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 11. API Endpoints
The platform exposes three basic GET endpoints:

### 1. Welcome Endpoint
*   **Route:** `GET /`
*   **Expected Response:**
    ```json
    {
      "message": "Welcome to Solar & Wind Deployment Intelligence Platform"
    }
    ```

### 2. Health Check Endpoint
*   **Route:** `GET /health`
*   **Expected Response:**
    ```json
    {
      "status": "Running"
    }
    ```

### 3. About Endpoint
*   **Route:** `GET /about`
*   **Expected Response:**
    ```json
    {
      "project": "Solar & Wind Deployment Intelligence Platform"
    }
    ```

## 12. Swagger API Documentation
How to test using Swagger UI:
1. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your web browser.
2. Select any endpoint (e.g., `GET /health` or `GET /about`) to expand it.
3. Click the **Try it out** button in the top-right of the endpoint section.
4. Click the blue **Execute** button.
5. Scroll down to review the **Response body** showing the JSON output and verify the **Response headers** show a `200` status code.

## 13. API Testing
You can manually verify the API endpoints directly in your browser or through tools like Postman:
*   Accessing [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) should display:
    ```json
    {"status": "Running"}
    ```
*   Accessing [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about) should display:
    ```json
    {"project": "Solar & Wind Deployment Intelligence Platform"}
    ```

## 14. Assignment Result
The FastAPI web server has been successfully configured, installed, and executed on the local environment. Both mandatory GET endpoints (`/health` and `/about`) along with the optional root endpoint (`/`) were successfully implemented, yielding the exact JSON responses and HTTP status codes (200 OK) required by the assignment guidelines.

## 15. Conclusion
Through this internship assignment, key learning outcomes were successfully demonstrated:
1. Setting up a local development environment with virtual environments in Windows.
2. Initializing a FastAPI application with custom title, version, and description metadata.
3. Defining REST API GET route decorators and mapping them to Python handler functions.
4. Structuring clean JSON dictionary responses in Python that FastAPI handles automatically.
5. Deploying and running Uvicorn as a local web server with auto-reload capabilities.
6. Testing and verifying REST APIs using the automatic interactive Swagger UI documentation.
