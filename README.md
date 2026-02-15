# E-commerce-Product-API
Model created:: Product and Category
Serializers created:: ProductSerializer, CategorySerializer
Views::
       Product_list(GET,POST)
       Product_detail(GET,PUT,DELETE)
       Category_list(GET,POST)
URLS::: path=>product and category urls

# Update done on 15th
Implimented the cors,permission,jwt and cors=>default auth and permission classes
created UserSerializer to definenusername and password and kwargs permission.

Refactored the categoryView to use generic classes CategoryListView & CreateUserView with updated permissions
Updated urls to include create user,token and token refresh

Tested the authenticated views using token on postman to access products
 