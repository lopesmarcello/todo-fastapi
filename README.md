# FastAPI Todo API with Multi-Tenancy

A production-ready FastAPI application demonstrating user authentication, multi-tenancy, and database integration.

## Overview

This project showcases modern FastAPI development with enterprise-grade features:

- **User Authentication**: JWT-based authentication with secure password hashing
- **Multi-Tenancy**: User-isolated data access ensuring privacy and security
- **Database Integration**: SQLAlchemy ORM with Alembic migrations
- **RESTful API**: Complete CRUD operations with proper HTTP status codes
- **Structured Architecture**: Clean project organization following FastAPI best practices


## Project Structure

```
fastapi-project/
├── app/
│   ├── api/          # API routes and endpoints
│   │   ├── v1/       # API version 1
│   │   │   ├── endpoints/  # Route handlers
│   │   │   │   ├── auth.py    # Authentication endpoints
│   │   │   │   └── todos.py   # Todo CRUD operations
│   │   │   └── api.py         # Route aggregation
│   │   └── deps.py    # Dependencies (auth, database)
│   ├── core/         # Core functionality
│   │   ├── config.py  # Application settings
│   │   ├── database.py # Database configuration
│   │   └── security.py # Security utilities
│   ├── models/       # SQLAlchemy database models
│   │   ├── user.py    # User model with relationships
│   │   └── todo.py    # Todo model with foreign keys
│   ├── schemas/      # Pydantic schemas for validation
│   │   ├── user.py    # User schemas (create, response)
│   │   └── todo.py    # Todo schemas (create, response)
│   └── main.py       # FastAPI application entry point
├── alembic/          # Database migrations
│   ├── versions/     # Migration files
│   └── env.py        # Alembic configuration
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Features

### Authentication & Security
- **JWT Token Authentication**: Secure stateless authentication with Bearer tokens
- **Password Hashing**: bcrypt-based secure password storage
- **User Registration**: Email-based user account creation
- **Token Expiration**: Configurable access token lifetime

### Multi-Tenancy
- **User Isolation**: Each user can only access their own data
- **Secure Filters**: Automatic filtering of data by owner_id
- **Authorization Middleware**: Dependency-based authentication checks

### Database Management
- **SQLAlchemy ORM**: Type-safe database operations
- **Alembic Migrations**: Database schema versioning
- **PostgreSQL Ready**: Configurable database backend (SQLite for development)
- **Relationship Management**: Proper foreign key constraints and relationships

### API Endpoints
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User authentication
- `GET /api/v1/todos/` - List user's todos
- `POST /api/v1/todos/` - Create new todo
- `GET /api/v1/todos/{id}` - Get specific todo
- `PUT /api/v1/todos/{id}` - Update todo
- `DELETE /api/v1/todos/{id}` - Delete todo

## Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM with async support
- **PostgreSQL** - Production-ready relational database (configurable)
- **Alembic** - Database migration tool
- **Pydantic** - Data validation using Python type annotations
- **JWT (python-jose)** - JSON Web Token implementation
- **bcrypt** - Password hashing library
- **Uvicorn** - ASGI server

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost/dbname
# For development: DATABASE_URL=sqlite:///./test.db

# Security
SECRET_KEY=your-secret-key-here

# JWT Configuration
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Application
PROJECT_NAME=Todo API V1
```

### Database Setup

#### PostgreSQL (Production)
1. Install PostgreSQL and create a database
2. Update `DATABASE_URL` in your `.env` file
3. Install the PostgreSQL driver: `pip install psycopg2-binary`

#### SQLite (Development)
- Default configuration uses SQLite for easy setup
- Database file: `./test.db`

### Running Migrations

```bash
# Generate migration for model changes
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your configuration

# Run database migrations
alembic upgrade head

# Start the development server
uvicorn app.main:app --reload

# Access the API
# API Documentation: http://localhost:8000/docs
# Interactive Docs: http://localhost:8000/redoc
```

## Usage Examples

### Register a User
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepassword"}'
```

### Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword"
```

### Create Todo (Authenticated)
```bash
curl -X POST "http://localhost:8000/api/v1/todos/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "description": "Complete the tutorial", "completed": false}'
```

## Development

This project demonstrates:
- **Clean Architecture**: Separation of concerns with layers
- **Dependency Injection**: FastAPI's powerful DI system
- **Type Safety**: Full type hints throughout
- **Testing Ready**: Structure optimized for unit testing
- **Production Deployment**: Configurable for production environments
