# 📘 Modular Blogging Platform Backend (Django + DRF)

### 👤 Author: **Shubh Gupta**  
### 🗂️ System Design Project Submission  
### 🧰 Backend Framework: **Django (Python) + Django REST Framework**

---

# 🚀 1. Project Overview

This project is a fully functional **Blogging Platform Backend**, designed using **Django** and **DRF** with a clean **modular architecture**, well-structured **database models**, and secure **JWT authentication**.

### ✅ Features:
- Role-based authentication (Admin, Author, Reader)
- Post creation, editing, publishing
- Tags + search + filtering
- Commenting system
- Like system (no duplicate likes)
- Analytics (views, likes, comments)
- JWT Authentication
- Unit test cases (pytest)
- Environment-based configuration

---

# 🧱 2. System Architecture

apps/
│
├── accounts/ → Custom User model + roles
├── blog/ → Posts & Tags
├── comments/ → Comment system
├── interactions/ → Likes
└── analytics/ → Event logging

yaml
Copy code

Other important components:

blogging_projects/ → Django settings, URLs, WSGI
tests/ → Complete unit test suite
.env → Environment variables
requirements.txt → Python dependencies
docker-compose.yml → Optional PostgreSQL container

markdown
Copy code

---

# 🧩 3. Key Features

## 🔐 Authentication & Authorization
- Custom user model  
- JWT tokens  
- Roles:
  - **Admin** → full access  
  - **Author** → create/edit posts  
  - **Reader** → view-only  

## 📝 Posts & Tags
- CRUD operations  
- Publish/draft state  
- Automatic slug generation  
- Tagging system  
- Search in title/content/excerpt  
- Filter by tag/author/status  

## 💬 Comments
- Add comments  
- Auto-approved  
- Comment count saved in Post  

## ❤️ Likes
- Like/unlike posts  
- Prevent duplicate likes  
- Like count stored in post  

## 👀 Analytics
Tracks:
- Views  
- Likes  
- Comments  

All events stored for insights.

---

# 🛠 4. Technology Stack

| Category | Technology |
|----------|------------|
| Backend | Django |
| API Framework | Django REST Framework |
| Database | PostgreSQL |
| Authentication | SimpleJWT |
| Testing | Pytest + pytest-django |
| Environment | python-dotenv |
| Optional | Docker Compose |

---

# 🗄️ 5. Database Schema Overview

## **User**
- username  
- email  
- password  
- role  

## **Post**
- title  
- slug  
- content  
- excerpt  
- status  
- published_at  
- FK → author  
- views_count  
- likes_count  
- comments_count  

## **Tag**
- name  
- slug  

## **Comment**
- FK → post  
- FK → user  
- content  
- approved  

## **Like**
- FK → post  
- FK → user  
- `unique together (user, post)`  

## **Event**
- FK → post  
- FK → user  
- event_type (view/like/comment)

---

# 🧰 6. How to Set Up & Run Locally

## 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd blogging_project
```
## 2️⃣ Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
## 3️⃣ Install dependencies
```bash
Copy code
pip install -r requirements.txt
```
## 4️⃣ Create a .env file
```bash
POSTGRES_DB=blogging
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=secret-key
DJANGO_DEBUG=1
```
## 5️⃣ Start PostgreSQL (optional, using Docker)
```bash
Copy code
docker compose up -d
```
## 6️⃣ Apply migrations
```bash
python3 manage.py migrate
```
## 7️⃣ Create admin user
```bash
python3 manage.py createsuperuser
```
## 8️⃣ Start the server
```bash
python3 manage.py runserver
Visit:

Admin → http://127.0.0.1:8000/admin

Posts API → http://127.0.0.1:8000/api/v1/posts/
```

## 🔐 7. Authentication (JWT)
## Get Access + Refresh Token
```bash
POST /api/v1/auth/token/
Body:
{
  "username": "your_username",
  "password": "your_password"
}
Then use:

Authorization: Bearer <access_token>
```
## 🧪 8. Running Unit Tests
This project uses pytest.

Run all tests:
```bash
pytest -q
```
Run with coverage:
```bash
pytest --cov=apps
```
Run tests for a specific module:
```bash
pytest tests/test_posts.py
```
Test files included:
tests/
├── test_auth.py
├── test_posts.py
├── test_comments.py
├── test_tags.py
├── test_likes.py
└── test_analytics.py
## 📦 9. Dependencies
All dependencies are inside requirements.txt.

Major ones:
django

djangorestframework

djangorestframework-simplejwt

psycopg2-binary

django-filter

pytest

pytest-django

python-dotenv

Install them using:

```bash
pip install -r requirements.txt
```
## 🌱 10. Environment Variables
Required:

```nginx
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
DJANGO_SECRET_KEY
DJANGO_DEBUG
```
It's recommended to include a .env.example.
