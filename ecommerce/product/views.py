from rest_framework.response import Response
from .models import  Product ,Category 
from .serializers import ProductSerializer ,CategorySerializer,UserSerializer,ResetPassword
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter
from .paginations import CustomPagination
from .permissions import IsAdmin
    
class CreateUserView(generics.CreateAPIView):
   queryset= User.objects.all()
   serializer_class= UserSerializer
   permission_classes= [AllowAny]

class CategoryListView(generics.ListCreateAPIView):
   queryset= Category.objects.all()
   serializer_class = CategorySerializer
   pagination_class= CustomPagination
   def get_permissions(self):
      if self.request.method in ['POST']:
         return[IsAuthenticated()]
      return[AllowAny()]
   
class CategoryView(generics.RetrieveUpdateDestroyAPIView):
   queryset=Category.objects.all()
   serializer_class= CategorySerializer
   lookup_field= 'pk'

   def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated()]
        return [AllowAny()]

class ProductListView(generics.ListCreateAPIView):
   queryset=Product.objects.all()
   serializer_class=ProductSerializer
   
   filter_backends= [DjangoFilterBackend,SearchFilter,OrderingFilter]
   filterset_fields=['category_id']
   filterset_class= ProductFilter
   search_fields= ['name']
   ordering_fields=['created_at']
   pagination_class = CustomPagination


   
   def get_queryset(self):
      return Product.objects.all()
   
   def get_permissions(self):
      if self.request.method=='POST':
         return [IsAdmin()]
      return [AllowAny()]
   
   def perform_create(self, serializer):
      if serializer.is_valid():
         serializer.save()
      else:
         return serializer.errors()
      
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   lookup_field = "pk"

   def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]
        return [AllowAny()]      

class ResetPasswordView(generics.UpdateAPIView):
   serializer_class=ResetPassword
   permission_classes = [IsAuthenticated]

   def get_object(self):
      return self.request.user
   
   def update(self,request,*args,**Kwargs):
      user= self.get_object()
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      if not user.check_password(serializer.validated_data["old_password"]):
         return Response("Password did not match" ,status=status.HTTP_400_BAD_REQUEST)
      
      user.set_password(serializer.validated_data["new_password"])
      user.save()
      return Response("password reset succesful", status=status.HTTP_200_OK)