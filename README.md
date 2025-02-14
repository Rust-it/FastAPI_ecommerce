# FastAPI E-commerce Backend

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

Современный бэкенд для электронной коммерции с использованием FastAPI, PostgreSQL и Docker. Проект поддерживает полный цикл управления пользователями, товарами, заказами и отзывами.

## 🌟 Особенности :cite[1]:cite[3]:cite[5]
- **Аутентификация JWT** с разделением ролей (админ/продавец/покупатель)
- **CRUD операции** для:
  - Товаров (с категориями и фильтрацией)
  - Пользователей (регистрация, профиль, адреса доставки)
  - Корзины покупок и заказов
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

# 2. Настроить окружение
cp .env.example .env
# Заполнить SECRET_KEY, DB_* параметры в .env

# 3. Запустить в Docker
docker-compose -f docker-compose.prod.yml up -d --build

# 4. Применить миграции
docker-compose exec web alembic upgrade head