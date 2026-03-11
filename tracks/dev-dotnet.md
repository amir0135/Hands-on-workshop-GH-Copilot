# Developers Hackathon - .NET Track 👩‍💻👨🏾‍💻
Welcome to the .NET Developers Hackathon. Build a retail store application using **.NET Core/ASP.NET Core** for the backend, **React** for the frontend, and **SQLite** for the database.

## Development Environment 💻
**Prerequisites:**
- [.NET 8 SDK](https://dotnet.microsoft.com/download) or later
- [Node.js](https://nodejs.org/) (v18 or later) for React frontend
- VS Code or Visual Studio
- GitHub Copilot extension (recommended)
- Git installed locally

**Recommended VS Code Extensions:**
- C# Dev Kit
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

### 2. Verify .NET Installation
```bash
dotnet --version  # Should show 8.0 or later
```

### 3. Create the Project Structure
```bash
# Create a new ASP.NET Core Web API project
dotnet new webapi -n RetailStoreAPI
cd RetailStoreAPI

# Add required NuGet packages
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
dotnet add package Microsoft.EntityFrameworkCore.Design
dotnet add package Microsoft.EntityFrameworkCore.Tools

# For Excel/PDF export (optional)
dotnet add package ClosedXML
dotnet add package QuestPDF
```

### 4. Create React Frontend
```bash
# In the project root (not in RetailStoreAPI)
npx create-react-app retail-store-ui
cd retail-store-ui

# Install additional packages
npm install axios react-router-dom
```

### 5. Configure SQLite Database
In your `appsettings.json`:
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Data Source=retailstore.db"
  }
}
```

# Challenge 1: Retail Store App 🌐

Build a web application for managing customers, products, and purchase orders.

**Tech Stack:**
- **Backend:** ASP.NET Core Web API
- **Frontend:** React
- **Database:** SQLite with Entity Framework Core
- **ORM:** Entity Framework Core

## Functional Requirements

### 1. User Interface
- React-based SPA (Single Page Application)
- Intuitive and user-friendly design
- Responsive layout

### 2. Customer Management
- **Model Properties:** Id, Name, Surname, Address, BirthDate, Email
- CRUD operations (Create, Read, Update, Delete)
- Email validation
- RESTful API endpoints

### 3. Product Management
- **Model Properties:** Id, Name, Description, Price
- CRUD operations
- Search functionality by Id and Name
- RESTful API endpoints

### 4. Order Management
- **Model Properties:** Id, OrderNumber, PurchaseDate, CustomerId, ProductIds
- CRUD operations
- Search by OrderNumber and Customer Name
- RESTful API endpoints

### 5. Reporting
- Export customers to Excel and PDF
- Export purchase orders to Excel and PDF

## Implementation Guide

### Backend Structure (ASP.NET Core)
```
RetailStoreAPI/
├── Controllers/
│   ├── CustomersController.cs
│   ├── ProductsController.cs
│   └── PurchaseOrdersController.cs
├── Models/
│   ├── Customer.cs
│   ├── Product.cs
│   └── PurchaseOrder.cs
├── Data/
│   └── ApplicationDbContext.cs
├── Services/
│   └── ExportService.cs
└── Program.cs
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

### Database Setup with EF Core
```bash
# Create initial migration
dotnet ef migrations add InitialCreate

# Apply migration and create database
dotnet ef database update
```

# Challenge 2: Application Testing 🧪

### Backend Testing
```bash
# Create test project
dotnet new xunit -n RetailStoreAPI.Tests

# Add test packages
cd RetailStoreAPI.Tests
dotnet add package Microsoft.EntityFrameworkCore.InMemory
dotnet add package Moq
dotnet add reference ../RetailStoreAPI/RetailStoreAPI.csproj
```

**Test Coverage:**
- Unit tests for Controllers
- Repository/Service layer tests
- Model validation tests

### Frontend Testing
```bash
# In retail-store-ui directory
npm install --save-dev @testing-library/react @testing-library/jest-dom
```

# Challenge 3: CI with GitHub Actions 🚀

Create `.github/workflows/dotnet-ci.yml`:

```yaml
name: .NET CI

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
    
    - name: Setup .NET
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: '8.0.x'
    
    - name: Restore dependencies
      run: dotnet restore RetailStoreAPI/RetailStoreAPI.csproj
    
    - name: Build
      run: dotnet build RetailStoreAPI/RetailStoreAPI.csproj --no-restore
    
    - name: Test
      run: dotnet test RetailStoreAPI.Tests/RetailStoreAPI.Tests.csproj --no-build --verbosity normal
    
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
- Tech stack: ASP.NET Core + React + SQLite
- Database schema (ER diagram)
- API endpoints documentation
- Setup and installation steps
- Build commands: `dotnet build`, `npm run build`
- Test commands: `dotnet test`, `npm test`
- Run commands: `dotnet run`, `npm start`

# GitHub Copilot Assistance 🤖

## Sample Prompts for .NET Development

### Project Setup
- "Create an ASP.NET Core Web API project structure"
- "Configure Entity Framework Core with SQLite"
- "Set up CORS for React frontend in ASP.NET Core"

### Models & Database
- "Generate a Customer model with Id, Name, Surname, Address, BirthDate, Email with data annotations"
- "Create a Product model with Id, Name, Description, Price"
- "Generate a PurchaseOrder model with relationships to Customer and Products"
- "Create ApplicationDbContext for Entity Framework Core with Customer, Product, and PurchaseOrder"
- "Add EF Core migration for all models"

### Controllers & API
- "Generate a CustomersController with CRUD endpoints using Entity Framework"
- "Create a ProductsController with GET, POST, PUT, DELETE actions"
- "Add search functionality to ProductsController for Id and Name"
- "Generate async API endpoints for PurchaseOrder management"

### Validation
- "Add data validation attributes to Customer model for email format"
- "Implement model validation in ASP.NET Core controllers"

### Export Features
- "Implement Excel export for Customer list using ClosedXML"
- "Generate PDF report for purchase orders using QuestPDF"
- "Create an ExportService class for data export functionality"

### React Frontend
- "Create a React component for displaying customer list with table"
- "Generate a form component for adding/editing customers with validation"
- "Create an axios service for API calls to ASP.NET Core backend"
- "Build a product search component with React hooks"

### Testing
- "Generate xUnit tests for CustomersController"
- "Create unit tests for Customer model validation"
- "Write integration tests for Product API endpoints with InMemory database"

### CI/CD
- "Create a GitHub Actions workflow for building and testing an ASP.NET Core application"
- "Add React build steps to GitHub Actions workflow"

## Running the Application

### Backend
```bash
cd RetailStoreAPI
dotnet run
# API will be available at https://localhost:5001
```

### Frontend
```bash
cd retail-store-ui
npm start
# React app will be available at http://localhost:3000
```

💡**Tips:**
- Use GitHub Copilot Chat to explain Entity Framework concepts
- Ask Copilot to help debug CORS issues between React and ASP.NET
- Request code reviews and optimization suggestions
- Use Copilot to generate sample data seeders
