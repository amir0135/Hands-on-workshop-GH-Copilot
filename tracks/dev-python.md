# Developers Hackathon - Python Track 👩‍💻👨🏾‍💻
Welcome to the Python Developers Hackathon. Build a retail store application using **Python/FastAPI** (or Flask) for the backend, **React** for the frontend, and **SQLite** for the database.

## Development Environment 💻
**Prerequisites:**
- [Python 3.9+](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/) (v18 or later) for React frontend
- VS Code or PyCharm
- GitHub Copilot extension (recommended)
- Git installed locally

**Recommended VS Code Extensions:**
- Python
- Pylance
- GitHub Copilot
- ES7+ React/Redux/React-Native snippets
- SQLite Viewer

## Setup Instructions 🛠️

### 1. Clone the Repository
```bash
git clone https://github.com/hosseinzahed/demant-github-hackathon.git
cd demant-github-hackathon
git checkout -b team1  # Replace 'team1' with your team name
```

### 2. Verify Python Installation
```bash
python --version  # Should show 3.9 or later
# or
python3 --version
```

### 3. Create Python Backend Project

#### Option A: FastAPI (Recommended)
```bash
# Create project directory
mkdir retail-store-api
cd retail-store-api

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install fastapi uvicorn sqlalchemy pydantic python-multipart

# For Excel/PDF export
pip install openpyxl reportlab pandas

# For CORS
pip install fastapi[all]

# Create requirements.txt
pip freeze > requirements.txt
```

#### Option B: Flask
```bash
# Create project directory
mkdir retail-store-api
cd retail-store-api

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install required packages
pip install flask flask-sqlalchemy flask-cors

# For Excel/PDF export
pip install openpyxl reportlab pandas

pip freeze > requirements.txt
```

### 4. Create React Frontend
```bash
# In the project root directory
npx create-react-app retail-store-ui
cd retail-store-ui

# Install additional packages
npm install axios react-router-dom
```

# Challenge 1: Retail Store App 🌐

Build a web application for managing customers, products, and purchase orders.

**Tech Stack:**
- **Backend:** FastAPI or Flask
- **Frontend:** React
- **Database:** SQLite with SQLAlchemy ORM
- **ORM:** SQLAlchemy

## Functional Requirements

### 1. User Interface
- React-based SPA (Single Page Application)
- Intuitive and user-friendly design
- Responsive layout

### 2. Customer Management
- **Model Properties:** id, name, surname, address, birth_date, email
- CRUD operations (Create, Read, Update, Delete)
- Email validation
- RESTful API endpoints

### 3. Product Management
- **Model Properties:** id, name, description, price
- CRUD operations
- Search functionality by id and name
- RESTful API endpoints

### 4. Order Management
- **Model Properties:** id, order_number, purchase_date, customer_id, product_ids
- CRUD operations
- Search by order_number and customer name
- RESTful API endpoints

### 5. Reporting
- Export customers to Excel and PDF
- Export purchase orders to Excel and PDF

## Implementation Guide

### Backend Structure (FastAPI)
```
retail-store-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── customers.py
│   │   ├── products.py
│   │   └── orders.py
│   └── services/
│       └── export_service.py
├── requirements.txt
└── retailstore.db (created automatically)
```

### Backend Structure (Flask)
```
retail-store-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── database.py
│   └── services/
│       └── export_service.py
├── run.py
├── requirements.txt
└── retailstore.db (created automatically)
```

### Frontend Structure (React)
```
retail-store-ui/
├── src/
│   ├── components/
│   │   ├── Customers/
│   │   ├── Products/
│   │   └── Orders/
│   ├── services/
│   │   └── api.js
│   ├── App.js
│   └── index.js
└── package.json
```

### Database Setup with SQLAlchemy

**FastAPI Example (database.py):**
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./retailstore.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

# Challenge 2: Application Testing 🧪

### Backend Testing
```bash
# Install testing packages
pip install pytest pytest-cov httpx

# For FastAPI
pip install pytest-asyncio

# Create tests directory
mkdir tests
```

**Test Structure:**
```
tests/
├── __init__.py
├── test_customers.py
├── test_products.py
└── test_orders.py
```

**Test Coverage:**
- Unit tests for API endpoints
- Model validation tests
- Database operation tests

### Frontend Testing
```bash
# In retail-store-ui directory
npm install --save-dev @testing-library/react @testing-library/jest-dom
```

**Run Tests:**
```bash
# Backend
pytest --cov=app tests/

# Frontend
cd retail-store-ui
npm test
```

# Challenge 3: CI with GitHub Actions 🚀

Create `.github/workflows/python-ci.yml`:

```yaml
name: Python CI

on:
  push:
    branches: [ main, team* ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        cd retail-store-api
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        cd retail-store-api
        pytest --cov=app tests/
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    
    - name: Install frontend dependencies
      run: |
        cd retail-store-ui
        npm ci
    
    - name: Build frontend
      run: |
        cd retail-store-ui
        npm run build
    
    - name: Test frontend
      run: |
        cd retail-store-ui
        npm test -- --watchAll=false
```

# Challenge 4: Documentation 📝

Create `DOCS.md` including:
- Application architecture overview
- Tech stack: FastAPI/Flask + React + SQLite
- Database schema (ER diagram)
- API endpoints documentation (use FastAPI's automatic Swagger docs at `/docs`)
- Setup and installation steps
- Virtual environment setup
- Build commands
- Test commands: `pytest`, `npm test`
- Run commands: `uvicorn app.main:app --reload` or `python run.py`, `npm start`

# GitHub Copilot Assistance 🤖

## Sample Prompts for Python Development

### Project Setup
- "Create a FastAPI project structure with SQLAlchemy"
- "Set up Flask application with SQLAlchemy and SQLite"
- "Configure CORS for React frontend in FastAPI"

### Models & Database
- "Generate a Customer SQLAlchemy model with id, name, surname, address, birth_date, email"
- "Create a Product model using SQLAlchemy with id, name, description, price"
- "Generate a PurchaseOrder model with relationships to Customer and Products in SQLAlchemy"
- "Create database initialization script for SQLAlchemy models"

### Pydantic Schemas (FastAPI)
- "Generate Pydantic schemas for Customer model with validation"
- "Create Pydantic schema for Product with price validation"
- "Add email validation to Customer Pydantic schema"

### Routes & API
- "Generate FastAPI router for Customer CRUD operations"
- "Create Flask routes for Product management with GET, POST, PUT, DELETE"
- "Add search endpoint for products by id and name in FastAPI"
- "Generate async CRUD endpoints for PurchaseOrder in FastAPI"

### Validation
- "Add email validation to Customer model using Pydantic validators"
- "Implement input validation for Product price field"

### Export Features
- "Implement Excel export for Customer list using openpyxl"
- "Generate PDF report for purchase orders using reportlab"
- "Create an export service class for data export to Excel and PDF"

### React Frontend
- "Create a React component for displaying customer list"
- "Generate a form component for adding/editing customers with validation"
- "Create an axios service for API calls to FastAPI backend"
- "Build a product search component with React hooks"

### Testing
- "Generate pytest tests for Customer API endpoints"
- "Create unit tests for Product model validation"
- "Write integration tests for FastAPI endpoints with TestClient"
- "Generate pytest fixtures for database testing"

### CI/CD
- "Create a GitHub Actions workflow for Python FastAPI application with pytest"
- "Add React build steps to GitHub Actions workflow"

## Running the Application

### Backend (FastAPI)
```bash
cd retail-store-api
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn app.main:app --reload
# API will be available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### Backend (Flask)
```bash
cd retail-store-api
source venv/bin/activate  # or venv\Scripts\activate on Windows
python run.py
# API will be available at http://localhost:5000
```

### Frontend
```bash
cd retail-store-ui
npm start
# React app will be available at http://localhost:3000
```

💡**Tips:**
- Use GitHub Copilot Chat to explain SQLAlchemy relationships
- Ask Copilot to help debug CORS issues between React and FastAPI/Flask
- Request code reviews and optimization suggestions
- Use Copilot to generate sample data seeders
- Take advantage of FastAPI's automatic API documentation at `/docs`
