# E-commerce-Product-API
Model created:: Product and Category
Serializers created:: ProductSerializer, CategorySerializer
Views:
       Product_list(GET,POST)
       Product_detail(GET,PUT,DELETE)
       Category_list(GET,POST)
URLS: path=>product and category urls

# Update done on 15th
Implimented the cors,permission,jwt and cors=>default auth and permission classes
created UserSerializer to definenusername and password and kwargs permission.

Refactored the categoryView to use generic classes CategoryListView & CreateUserView with updated permissions
Updated urls to include create user,token and token refresh

Tested the authenticated views using token on postman to access products
 

# Update done on 17th

Implimented custom Filters for price and quantity and inbuilt django filters for product category by category_id,name and time created.
Tested the search Filter using products added via postman.

# Created the CategoryView: Endpoints
GET /categories/<id>/
PUT /categories/<id>/
DELETE /categories/<id>/

# Description:
Allows retrieving a single category by ID
Updating a category
Deleting a category

# List Products / Create Product Endpoints
GET /products/
POST /products/
# Description
GET returns all products (public access)
POST creates a new product (authentication required)
 
 # Filtering, Searching & Ordering (Products)
# Filter by Category
GET /products/?category_id=1
# Search by Product Name
GET /products/?search=iphone
# Order by Created Date
GET /products/?ordering=created_at
# Descending order:
GET /products/?ordering=-created_at

# Technologies Used
Django
Django REST Framework (DRF)
django-filter
DRF SearchFilter & OrderingFilter
Token Authentication 