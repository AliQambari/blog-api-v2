# 📝 Django Blog Project – Dual API Version (Manual & DRF)

This is a simple blog project built with **Django**, featuring two parallel API versions:

- `api/v1/` → Manually implemented views (no DRF)
- `api/v2/` → Modern RESTful API built using **Django REST Framework (DRF)**

Technologies Used:
**Django 4.x**
**Django REST Framework (DRF)**
**drf-yasg (Swagger support)**
**Python 3.8.**5**


Version 1: Manual Views (api/v1/)
| Method | Endpoint                           | Description                          |
| ------ | ---------------------------------- | ------------------------------------ |
| GET    | `/api/v1/posts/`                   | List all posts                       |
| POST   | `/api/v1/posts/`                   | Create a new post                    |
| GET    | `/api/v1/posts/<id>/`              | Retrieve a specific post by ID       |
| PATCH  | `/api/v1/posts/<id>/`              | Update a specific post (partial)     |
| DELETE | `/api/v1/posts/<id>/`              | Delete a post                        |
| GET    | `/api/v1/categories/`              | List all categories                  |
| GET    | `/api/v1/categories/<id>/`         | Retrieve a specific category by ID   |
|  GET   | `/api/v1/posts/category/<cat_id>/` | List posts under a specific category |




Version 2: DRF Views (api/v2/)
| Method | Endpoint                   | Description             |
| ------ | -------------------------- | ----------------------- |
| GET    | `/api/v2/posts/`           | List blog posts         |
| POST   | `/api/v2/posts/`           | Create new post         |
| GET    | `/api/v2/posts/<id>/`      | Retrieve a post         |
| PATCH  | `/api/v2/posts/<id>/`      | Update partial post     |
| DELETE | `/api/v2/posts/<id>/`      | Delete post             |
| GET    | `/api/v2/categories/`      | List categories         |
| POST   | `/api/v2/categories/`      | Create new category     |
| GET    | `/api/v2/categories/<id>/` | Retrieve category       |
| PATCH  | `/api/v2/categories/<id>/` | Update partial category |
| DELETE | `/api/v2/categories/<id>/` | Delete category         |
