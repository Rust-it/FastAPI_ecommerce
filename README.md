# FastAPI E-commerce Backend

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=SQLAlchemy&logoColor=FFFFFF)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=Redis&logoColor=FFFFFF)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=FFFFFF)
![NGINX](https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=FFFFFF)


Современный бэкенд для электронной коммерции с использованием FastAPI, PostgreSQL, SQLAlchemy, Redis, Docker, Gunicorn и Nginx. Проект поддерживает управление пользователями, категориями, товарами и отзывами с рейтингом.

## 🌟 Особенности:
- **Аутентификация JWT** с разделением ролей (админ/продавец/покупатель)
- **CRUD операции** для:
  - Товаров (с категориями и фильтрацией)
  - Пользователей (регистрация, профиль)
  - Отзывов и рейтингов товаров
- **Swagger/ReDoc документация** с возможностью тестирования API
- **Асинхронная архитектура** с поддержкой 1000+ RPS
- Готовые Docker-образы для production

## 🛠 Технологии
| Компонент       | Технологии                          |
|-----------------|-------------------------------------|
| Фреймворк       | FastAPI 0.109+                      |
| База данных     | PostgreSQL 15 + SQLAlchemy 2.0      |
| Аутентификация  | JWT + OAuth2PasswordBearer          |
| Кэширование     | Redis 7                             |
| Деплой          | Docker + Nginx + Gunicorn           |
| Мониторинг      | Prometheus + Grafana                |

## 🚀 Быстрый старт

### Предварительные требования
- Docker 24+
- Python 3.11+
- PostgreSQL 15

```bash
# 1. Клонировать репозиторий
git clone https://github.com/Rust-it/FastAPI_ecommerce.git
cd FastAPI_ecommerce

# 2. Запустить в Docker
docker-compose -f docker-compose.prod.yml up -d --build

# 3. Применить миграции
docker-compose exec web alembic upgrade head
```

### После запуска документация будет доступна:

* Swagger UI: http://localhost/docs или http://127.0.0.1/docs
* ReDoc: http://localhost/redoc или http://127.0.0.1/redoc