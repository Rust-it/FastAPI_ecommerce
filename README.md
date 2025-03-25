# FastAPI E-commerce Backend

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=SQLAlchemy&logoColor=FFFFFF)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=Redis&logoColor=FFFFFF)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=FFFFFF)
![NGINX](https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=FFFFFF)


Modern E-commerce Backend with FastAPI, PostgreSQL, SQLAlchemy, Redis, Docker, Gunicorn, and Nginx. The project supports user management, categories, products, and reviews with ratings.

## 🌟 Features:
- **JWT Authentication** with role-based access (admin/seller/customer)
- **CRUD Operations** for:
  - Products (with categories and filtering)
  - Users (registration, profile management)
  - Product reviews and ratings
- **Swagger/ReDoc API Documentation** with interactive testing
- **Asynchronous Architecture** supporting 1000+ RPS
- Pre-built Docker images for production

## 🛠 Technologies
| Component       | Technologies                          |
|-----------------|-------------------------------------|
| Framework       | FastAPI 0.109+                      |
| Database        | PostgreSQL 15 + SQLAlchemy 2.0      |
| Authentication  | JWT + OAuth2PasswordBearer          |
| Caching         | Redis 7                             |
| Deployment      | Docker + Nginx + Gunicorn           |

## 🚀 Quick Start

### Prerequisites
- Docker 24+
- Python 3.11+
- PostgreSQL 15

```bash
# 1. Clone repository
git clone https://github.com/Rust-it/FastAPI_ecommerce.git
cd FastAPI_ecommerce

# 2. Start with Docker
docker-compose -f docker-compose.prod.yml up -d --build

# 3. Apply migrations
docker-compose exec web alembic upgrade head
```

### After launching, the documentation will be available at:

* Swagger UI: http://localhost/docs or http://127.0.0.1/docs
* ReDoc: http://localhost/redoc or http://127.0.0.1/redoc