📘 Modular Blogging Platform Backend (Django + DRF)
👤 Author: Shubh Gupta
🗂️ System Design Project Submission
🧰 Backend Framework: Django (Python) + Django REST Framework
🚀 1. Project Overview

This project is a fully functional Blogging Platform Backend, designed using Django and Django REST Framework (DRF). It follows clean modular architecture, strong backend design principles, and well-structured database models.

✅ The system supports:

Role-based authentication

Post creation, editing, and publishing

Commenting system

Likes and user interactions

Analytics event logging

Tags and search

Cleanly structured API

Unit testing

Environment-based configuration

This backend can be used with React, Next.js, Flutter, or any frontend framework.

🧱 2. System Architecture
apps/
│
├── accounts/        → Custom User model + role-based permissions
├── blog/            → Posts, Tags, Publishing system
├── comments/        → Users can comment on posts
├── interactions/    → Like system
└── analytics/       → Event tracking (views, likes, comments)

Other components:
blogging_projects/ → Django core project (settings, urls, wsgi)
tests/             → All unit tests (pytest)
.env               → Environment configuration
docker-compose.yml → Optional PostgreSQL setup
requirements.txt   → Python dependencies

🧩 3. Key Features
🔐 Authentication & Authorization

Custom user model

JWT authentication

Role-based permissions:

Admin: Full access

Author: Create/edit/delete posts

Reader: Read-only

📝 Posts & Tags

Create, update, delete posts

Draft and published statuses

Automatic slug generation

Excerpts

Tagging system

Search and filter (title, content, tags, author)

💬 Comments

Add comments

Automatic approval

Comment count tracking

❤️ Likes (Interactions)

Like/unlike posts

Duplicate-like prevention

Like count stored in post

👀 Analytics

Tracks events including:

Views

Likes

Comments

All events stored for insights.

🛠 4. Technology Stack
Category	Technology
Backend	Django
API Framework	Django REST Framework
Database	PostgreSQL
Authentication	SimpleJWT
Container (Optional)	Docker + Docker Compose
Testing	Pytest + pytest-django
Environment	python-dotenv
🗄️ 5. Database Schema Overview
User

username

email

password

role (admin/author/reader)

Post

title

slug

content

excerpt

status (draft/published)

published_at

FK → author

counters → views, likes, comments

Tag

name

slug

Comment

FK → post

FK → user

content

approved

Like

FK → post

FK → user

Unique together constraint

Analytics Event

FK → post

FK → user

event_type (view/like/comment)

🧰 6. How to Set Up & Run Locally
1️⃣ Clone the Repository
git clone <your-repo-url>
cd blogging_project

2️⃣ Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Create a .env File

Create a file named .env:

POSTGRES_DB=blogging
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=secret-key
DJANGO_DEBUG=1

5️⃣ Run PostgreSQL via Docker (Optional but Recommended)
docker compose up -d


Check containers:

docker compose ps

6️⃣ Apply Migrations
python3 manage.py migrate

7️⃣ Create an Admin User
python3 manage.py createsuperuser

8️⃣ Start the Development Server
python3.manage.py runserver

Visit:

Admin Dashboard:
http://127.0.0.1:8000/admin/

API Posts Endpoint:
http://127.0.0.1:8000/api/v1/posts/

🔐 7. Authentication (JWT)
Get Token
POST /api/v1/auth/token/

Body:
{
  "username": "your_username",
  "password": "your_password"
}

Use Token
Authorization: Bearer <access_token>

🧪 8. Running Unit Tests

This project uses pytest.

✔ Run ALL tests:
pytest -q

✔ Run with coverage:
pytest --cov=apps

✔ Run tests for a specific app:
pytest apps/blog

Tests Included:
tests/
│
├── test_auth.py
├── test_posts.py
├── test_comments.py
├── test_likes.py
├── test_tags.py
└── test_analytics.py

📦 9. Dependencies

Defined in requirements.txt.

Key packages:

Django

djangorestframework

djangorestframework-simplejwt

psycopg2-binary

django-filter

pytest

pytest-django

python-dotenv

Install all dependencies:

pip install -r requirements.txt

🌱 10. Environment Variables

Required:

POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
DJANGO_SECRET_KEY
DJANGO_DEBUG


👉 Create .env.example so others understand what variables are needed.

🎉 11. Conclusion

This project provides:

Clean and scalable Django architecture

Modular design

Real-world blogging functionality

Secure authentication

Complete unit test coverage

Professional documentation