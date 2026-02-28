Ecommerce Product API
## Project Overview

Ecommerce Product API is a RESTful backend application built using Django 6 and Django REST Framework (DRF).

The API is designed to manage products in an e-commerce platform, allowing authenticated users to create, update, and delete products, while unauthenticated users can view and search available products.

This project demonstrates real-world backend development skills including:

RESTful API design
JWT authentication
Token-based security
Filtering and search
Pagination
CRUD operations
User registration and authentication

## Tech Stack

Framework: Django 6
API Framework: Django REST Framework
Authentication: JWT & Token Authentication
Database: SQLite
Language: Python

## Authentication & Permissions

The API implements secure authentication using:
JWT Authentication
Token Authentication

Authentication Endpoints:

Method	Endpoint	Description
POST	/login	Obtain JWT access & refresh token
POST	/token/refresh	Refresh JWT token
POST	/register	Register a new user

## Access Control

✅ Unauthenticated users can:
View products
Search products
Filter products

🔒 Only authenticated users can:
Create products
Update products
Delete products
Manage categories

## Database Models
🗂 Category Model
Field	Type
name	CharField (max_length=100)

📦 Product Model
Field	Type
name	CharField (max_length=100, required)
description	TextField
price	DecimalField (max_digits=10, decimal_places=2, required)
quantity	IntegerField (required)
category_id	IntegerField (nullable)
image	URLField (nullable)
created_at	DateTimeField (auto_now_add=True)
updated_at	DateTimeField (auto_now=True)

## 🌐 API Endpoints
📦 Product Endpoints
Method	 Endpoint	         Description	                   Auth Required
GET	    /product/	          List all products (Paginated)	  ❌
POST  	/product/	          Create new product	            ✅
GET	    /product/<id>/     	Retrieve product by ID        	❌
PUT   	/product/<id>/	    Update product	                ✅
DELETE	/product/<id>/	    Delete product	                ✅

🗂 Category Endpoints
Method	     Endpoint	       Description	         Auth Required
GET	       /category/	        List categories	      ❌
POST     	/category/	        Create category	      ✅
GET	      /category/<id>/	    Retrieve category	    ❌
PUT	      /category/<id>/	    Update category	      ✅
DELETE  	/category/<id>/	    Delete category	      ✅

Password-reset
Method	     Endpoint	       Description	         Auth Required
PUT      /reset_password/      reset password         ✅

{
    "old_password": "your_current_password",
    "new_password": "your_new_password"
}
## 🔎 Search & Filtering

The API supports advanced product querying:

🔍 Search
.Search by product name
.Partial match supported

Example:

GET /product/?search=phone

## 🎯 Filtering

.Filter by category
.Filter by price range

Examples:
GET /product/?category=1
GET /product/?min_price=100&max_price=1000

## 📄 Pagination

Product listing is paginated to improve performance when handling large datasets.

Example:

GET /product/?page=2

## 👤 User Management

User Registration
JWT Login
Token Refresh
Default Django User Model used

## ⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/frankkeybet/E-commerce-Product-API.git
cd E-commerce-Product-API
2️⃣ Create Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Create Superuser (Optional)
python manage.py createsuperuser
6️⃣ Start Development Server
python manage.py runserver

API will be available at:

http://127.0.0.1:8000/

## 🧪 Testing
You can test the API using:

Postman
cURL
Browser (for GET requests)
DRF Browsable API

## 🚀 Deployment Status

❌ Not yet deployed

Currently running in local development environment

## Database: SQLite

## 🔮 Future Improvements

Implement ForeignKey relationship for Category instead of IntegerField
Add Stock auto-reduction when order is placed
Deploy to production (Render / Heroku / PythonAnywhere)
Add product image upload instead of URL
Implement order management system
Add role-based permissions (Admin / Manager)