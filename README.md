# Construction Project Management API

A professional-grade, FastAPI-powered backend for comprehensive construction project management. This application provides secure user authentication, role-based access control, and complete project lifecycle management with daily progress tracking capabilities.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Quick Start Guide](#quick-start-guide)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Role-Based Access Control](#role-based-access-control)
- [Testing the API](#testing-the-api)
- [Using docs.json with Postman](#using-docsjson-with-postman)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Quick Start Guide

Get up and running with the Construction API in 5 minutes:

### 1. Clone and Setup
```bash
git clone https://github.com/your-organization/construction-api.git
cd construction-api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Database
```bash
# Create MySQL database
mysql -u root -p -e "CREATE DATABASE construction_api;"

# Copy and update .env
cp .env.example .env
# Edit .env with your MySQL credentials

# Run database schema
mysql -u your_user -p construction_api < database.sql
```

### 3. Start Server
```bash
cd api
uvicorn app.main:app --reload
```

Access the API at: **http://localhost:8000/docs**

### 4. Test with Default Admin
```bash
# Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"admin123"}'

# Use the token from response for authenticated requests
```

---

## Overview

The Construction Project Management API is a robust backend service designed to streamline construction project workflows. It enables seamless collaboration between administrators, project managers, and workers by providing a centralized platform for project management and daily progress tracking through Digital Progress Reports (DPRs).

### Key Capabilities

- **Secure Authentication:** JWT-based authentication mechanism for safe user access
- **Granular Permissions:** Role-based access control (RBAC) with three distinct user roles
- **Project Management:** Complete lifecycle management from planning to completion
- **Progress Tracking:** Daily progress reports with detailed work descriptions, weather conditions, and worker counts
- **RESTful API:** Standard REST conventions for easy integration with frontend applications

---

## Features

### Authentication & Authorization
- **User Registration:** New users can register with email and password
- **Secure Login:** JWT-based login system with token-based authentication
- **Password Security:** Passwords are hashed using industry-standard PBKDF2-SHA256 algorithm
- **Token-Based Authorization:** Each authenticated request includes a Bearer token for validation

### Project Management
- **Create Projects:** Admin and manager users can create new construction projects
- **Project Details:** Store project name, description, start date, end date, and status
- **Project Status Tracking:** Track projects through different states (planned, active, completed)
- **Update Projects:** Modify project details with proper authorization
- **Delete Projects:** Remove projects from the system (admin only)
- **List Projects:** View all projects with filtering by status and pagination support

### Daily Progress Reports (DPRs)
- **Submit Reports:** Workers can submit daily progress reports for ongoing projects
- **Report Details:** Capture work descriptions, weather conditions, and worker counts
- **Report Retrieval:** View all reports for a specific project with optional date filtering
- **Data Persistence:** All reports are stored with timestamps for audit trails

### Role-Based Access Control
- **Admin:** Full system access, can manage users, projects, and perform deletions
- **Manager:** Can create and edit projects, view all reports
- **Worker:** Can submit DPRs and view project information

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| **Framework** | FastAPI (Python 3.10+) |
| **Database** | MySQL 8.0+ |
| **ORM** | SQLAlchemy 2.0+ |
| **Authentication** | JWT (JSON Web Tokens) |
| **Password Hashing** | Passlib with PBKDF2-SHA256 |
| **Data Validation** | Pydantic v2 |
| **Web Server** | Uvicorn |
| **API Documentation** | Swagger UI / OpenAPI 3.0 |

---

## Project Structure

```
task-1/
├── api/
│   └── app/
│       ├── __pycache__/
│       ├── auth.py                 # Authentication and authorization logic
│       ├── database.py             # Database connection and session management
│       ├── main.py                 # FastAPI application entry point
│       ├── models/
│       │   ├── __init__.py
│       │   ├── USER.py             # User model with roles
│       │   ├── PROJECTS.py         # Project model
│       │   └── DRP.py              # Daily Report model
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── auth.py             # Authentication endpoints
│       │   ├── projects.py         # Project management endpoints
│       │   └── dpr.py              # DPR management endpoints
│       └── schemas/
│           ├── __init__.py
│           ├── LoginRequest.py
│           ├── RegisterRequest.py
│           ├── TokenResponse.py
│           ├── ProjectCreate.py
│           ├── ProjectUpdate.py
│           ├── ProjectResponse.py
│           ├── DPRCreate.py
│           └── DPRResponse.py
├── .env                            # Environment variables (not in version control)
├── .env.example                    # Example environment file
├── requirements.txt                # Python dependencies
├── database.sql                    # Database schema and initial data
├── seed.py                         # Database seeding script
├── docs.json                       # Postman collection
└── README.md                       # This file
```

---

## Prerequisites

Before setting up the project, ensure your system has the following:

### System Requirements
- **Operating System:** Linux, macOS, or Windows with WSL2
- **Python:** Version 3.10 or higher
- **MySQL Server:** Version 8.0 or higher
- **Memory:** Minimum 1GB RAM
- **Disk Space:** At least 500MB free space

### Required Tools
- **pip:** Python package manager (usually comes with Python)
- **MySQL Client:** For executing SQL scripts
- **Git:** For version control (optional but recommended)
- **cURL or Postman:** For testing API endpoints

### Verification Commands

```bash
# Check Python version
python --version

# Check pip installation
pip --version

# Check MySQL installation
mysql --version
```

---

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-organization/construction-api.git
cd construction-api
```

### Step 2: Create Virtual Environment

Creating an isolated Python environment is essential for managing project dependencies:

```bash
# Create virtual environment
python -m venv .venv

# Activate on Linux/macOS
source .venv/bin/activate

# Activate on Windows
.venv\Scripts\activate
```

**Note:** You should see `(.venv)` prefix in your terminal when activated.

### Step 3: Install Dependencies

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
# Check installed packages
pip list

# Test fastapi installation
python -c "import fastapi; print(f'FastAPI {fastapi.__version__} installed successfully')"
```

---

## Configuration

### Environment Variables Setup

1. **Copy the example environment file:**

   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file with your database credentials:**

   ```env
   # Database Configuration
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=construction_api

   # JWT Configuration
   SECRET_KEY=your-super-secret-key-change-this-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30

   # Security
   ROUNDS=29000
   SALT_SIZE=16
   ```

### .env File Details

| Variable | Purpose | Example |
|----------|---------|---------|
| `DB_USER` | MySQL username | `root` |
| `DB_PASSWORD` | MySQL password | `password123` |
| `DB_HOST` | MySQL host address | `localhost` |
| `DB_PORT` | MySQL port | `3306` |
| `DB_NAME` | Database name | `construction_api` |
| `SECRET_KEY` | JWT signing key | Generate a strong random string |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token validity period | `30` |

**Security Note:** Never commit the `.env` file to version control. Always use strong, randomly generated values for `SECRET_KEY` in production.

---

## Database Setup

### Step 1: Create MySQL Database

Connect to your MySQL server and create a new database:

```bash
mysql -u root -p
```

Then execute:

```sql
CREATE DATABASE construction_api;
```

### Step 2: Create Tables and Seed Data

Run the database schema script:

```bash
mysql -u your_mysql_user -p construction_api < database.sql
```

This script will:
- Create the `users` table with role support
- Create the `projects` table with status tracking
- Create the `daily_reports` table for DPR management
- Seed an initial admin user:
  - **Email:** admin@example.com
  - **Password:** admin123

### Step 3: Seed Additional Data (Optional)

To automatically populate the admin user:

```bash
python seed.py
```

### Database Schema Overview

#### Users Table
```
users
├── id (PK)
├── name (VARCHAR 100)
├── email (VARCHAR 100, UNIQUE)
├── password_hash (VARCHAR 255)
├── role (ENUM: admin, manager, worker)
└── created_at (TIMESTAMP)
```

#### Projects Table
```
projects
├── id (PK)
├── name (VARCHAR 200)
├── description (TEXT)
├── start_date (DATE)
├── end_date (DATE)
├── status (ENUM: planned, active, completed)
├── created_by (FK → users.id)
└── created_at (TIMESTAMP)
```

#### Daily Reports Table
```
daily_reports
├── id (PK)
├── project_id (FK → projects.id)
├── user_id (FK → users.id)
├── date (DATE)
├── work_description (TEXT)
├── weather (VARCHAR 100)
├── worker_count (INT)
└── created_at (TIMESTAMP)
```

---

## Running the Application

### Start the FastAPI Server

```bash
# Navigate to the api directory
cd api

# Start the server
uvicorn app.main:app --reload
```

### Expected Output

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [PID] using StatReload
INFO:     Started server process [PID]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Server Options

| Option | Purpose |
|--------|---------|
| `--reload` | Auto-restart on code changes (development only) |
| `--host 0.0.0.0` | Listen on all network interfaces |
| `--port 8080` | Use custom port (default: 8000) |

### Production Deployment

For production deployment, use:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## API Documentation

Once the server is running, access the API documentation at:

- **Swagger UI (Interactive):** http://localhost:8000/docs
- **ReDoc (Alternative UI):** http://localhost:8000/redoc
- **OpenAPI JSON Schema:** http://localhost:8000/openapi.json

The Swagger UI allows you to:
- View all available endpoints
- See request/response schemas
- Test endpoints directly from the browser
- View error codes and status messages

---

## API Endpoints

### Authentication Endpoints

#### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response (201 Created):**
```json
{
  "userId": 1,
  "message": "User registered successfully"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user_id": 1,
  "role": "worker"
}
```

### Project Endpoints

#### Create Project
```http
POST /projects
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Downtown Building Complex",
  "description": "A 20-story commercial building",
  "start_date": "2026-04-01",
  "end_date": "2027-12-31",
  "status": "planned"
}
```

**Required Role:** Admin, Manager

#### List Projects
```http
GET /projects?limit=10&offset=0&status=active
Authorization: Bearer {access_token}
```

#### Get Project Details
```http
GET /projects/{id}
Authorization: Bearer {access_token}
```

#### Update Project
```http
PUT /projects/{id}
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "status": "active",
  "description": "Updated description"
}
```

**Required Role:** Admin, Manager

#### Delete Project
```http
DELETE /projects/{id}
Authorization: Bearer {access_token}
```

**Required Role:** Admin

### Daily Progress Report (DPR) Endpoints

#### Create DPR
```http
POST /projects/{project_id}/dpr
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "date": "2026-03-13",
  "work_description": "Foundation work completed on north wing",
  "weather": "Sunny",
  "worker_count": 25
}
```

**Required Role:** Admin, Manager, Worker

#### List DPRs for Project
```http
GET /projects/{project_id}/dpr?date=2026-03-13
Authorization: Bearer {access_token}
```

---

## Role-Based Access Control

### Permission Matrix

| Action | Admin | Manager | Worker |
|--------|-------|---------|--------|
| Create Project | ✓ | ✓ | ✗ |
| Update Project | ✓ | ✓ | ✗ |
| Delete Project | ✓ | ✗ | ✗ |
| List Projects | ✓ | ✓ | ✓ |
| View Project | ✓ | ✓ | ✓ |
| Create DPR | ✓ | ✓ | ✓ |
| View DPR | ✓ | ✓ | ✓ |

### User Roles Explained

**Admin**
- Full system access
- Can manage all projects and users
- Can delete projects and users
- Can modify any DPR

**Manager**
- Can create and manage projects
- Can assign workers to projects
- Can view and manage DPRs
- Cannot delete projects

**Worker**
- Can submit DPRs for assigned projects
- Can view assigned projects
- Cannot create or modify projects

---

## Testing the API

### Method 1: Using Swagger UI (Recommended)

1. Start the server
2. Navigate to http://localhost:8000/docs
3. Click on an endpoint to expand it
4. Click "Try it out"
5. Enter the required parameters
6. Click "Execute"

### Method 2: Using cURL Commands

**Test Admin Login:**
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@example.com",
    "password": "admin123"
  }'
```

**Create a Project:**
```bash
curl -X POST http://localhost:8000/projects \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "name": "New Project",
    "description": "Project description",
    "start_date": "2026-04-01",
    "end_date": "2027-04-01",
    "status": "planned"
  }'
```

**Create a DPR:**
```bash
curl -X POST http://localhost:8000/projects/1/dpr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "date": "2026-03-13",
    "work_description": "Foundation work completed",
    "weather": "Sunny",
    "worker_count": 20
  }'
```

### Method 3: Using Postman

1. Import the `docs.json` file into Postman
2. Set the base URL to `http://localhost:8000`
3. Use the pre-configured requests in the collection

---

## Using docs.json with Postman

### Import Steps

1. **Open Postman**
2. **Click Import** in the top left
3. **Select "File"** tab
4. **Choose the `docs.json`** file from the project root
5. **Click Import**

### Configure Environment

1. Create a new environment in Postman
2. Set variables:
   - `base_url`: http://localhost:8000
   - `token`: (leave empty, will be populated after login)

3. **Use Token in Requests:**
   - In each request, set header: `Authorization: Bearer {{token}}`
   - The token will automatically populate after successful login

---

## Troubleshooting

### Common Issues and Solutions

#### 1. "ModuleNotFoundError: No module named 'fastapi'"
**Solution:**
```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### 2. "ERROR: Can't connect to MySQL server"
**Solution:**
```bash
# Verify MySQL is running
mysql -u root -p

# Check .env file has correct credentials
cat .env

# Test connection
mysql -h localhost -u your_user -p your_db
```

#### 3. "JWT Error: Invalid Token"
**Solution:**
- Ensure you're using the correct Authorization header format: `Authorization: Bearer {token}`
- Verify the token hasn't expired (default: 30 minutes)
- Log in again to get a fresh token

#### 4. "403 Forbidden: Insufficient permissions"
**Solution:**
- Verify your user role has permission for the action
- Check the Permission Matrix above
- Ensure you're logged in with the correct user account

#### 5. "Port 8000 already in use"
**Solution:**
```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```

---

## Contributing

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions

### Making Changes
1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -m "Add feature description"`
3. Push to branch: `git push origin feature/your-feature`
4. Submit pull request

---

## Support

For issues, questions, or suggestions:
- Check the Troubleshooting section above
- Review the API documentation at `/docs`
- Check existing issues in the repository

---

**Last Updated:** March 2026
**Version:** 1.0.0

