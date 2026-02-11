🚀 FastAPI Clean Architecture API

Authentication REST API built with FastAPI following a clean and modular structure.
This project demonstrates secure user authentication using JWT, password hashing, and Dockerized deployment.

🛠 Tech Stack

FastAPI

SQLAlchemy

SQLite

Passlib (bcrypt)

Python-JOSE (JWT)

Docker

Python 3.11

📦 Features

✅ User registration

✅ User login

✅ JWT access token generation

✅ Protected route (/auth/me)

✅ Password hashing with bcrypt

✅ Modular project structure

✅ Docker support

📁 Project Structure
app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── deps.py
├── auth.py
│
├── core/
│   └── config.py
│
└── routers/
    ├── auth.py
    └── users.py

🐳 Run with Docker

Build and start the application:

docker compose up --build


API will be available at:

http://localhost:8000/docs

💻 Run Locally (Without Docker)

Create virtual environment:

python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run server:

uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs

🔐 Authentication Flow
1️⃣ Register
POST /auth/register

2️⃣ Login
POST /auth/login


Response:

{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}

3️⃣ Access Protected Route
GET /auth/me


Add header:

Authorization: Bearer <access_token>

🔒 Security Details

Passwords hashed using bcrypt

JWT signed with HS256

Configurable secret key

Token expiration supported

Database session handled via dependency injection

📌 Purpose

This project was built as a backend portfolio project to demonstrate:

REST API design

Authentication best practices

Clean architecture principles

Dependency management

Docker containerization
