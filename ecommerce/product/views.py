from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Product ,Category 
from .serializers import ProductSerializer ,CategorySerializer,UserSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter


# Create your views here.
# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET': 
#      products = Product.objects.all()
#      serializer = ProductSerializer(products, many=True)
#      return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#       serializer = ProductSerializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data, status = status.HTTP_201_CREATED)
#       return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def product_detail(request, pk):
#    try:
#       product = Product.objects.get(pk=pk)
#    except Product.DoesNotExist:
#       return Response(status=status.HTTP_404_NOT_FOUND)
   
#    if request.method=='GET':
#       serializer = ProductSerializer(product)
#       return Response(serializer.data , status=status.HTTP_200_OK)
#    elif request.method=='PUT':
#       serializer = ProductSerializer(product, data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data , status=status.HTTP_200_OK)
#       return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
#    elif request.method=='DELETE':
#       product.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def category_list(request):
#     if request.method == 'GET':
#      categories = Category.objects.all()
#      serializer = CategorySerializer(categories, many=True)
#      return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#        serializer = CategorySerializer(data=request.data)
#        if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data ,status=status.HTTP_201_CREATED)
#        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class CreateUserView(generics.CreateAPIView):
   queryset= User.objects.all()
   serializer_class= UserSerializer
   permission_classes= [AllowAny]

class CategoryListView(generics.ListCreateAPIView):
   queryset= Category.objects.all()
   serializer_class = CategorySerializer
   permission_classes = [IsAuthenticated]

class CategoryView(generics.RetrieveUpdateDestroyAPIView):
   queryset=Category.objects.all()
   serializer_class= CategorySerializer
   lookup_field= 'pk'

class ProductListView(generics.ListCreateAPIView):
   queryset=Product.objects.all()
   serializer_class=ProductSerializer

   filter_backends= [DjangoFilterBackend,SearchFilter,OrderingFilter]
   filterset_fields=['category_id']
   filterset_class= ProductFilter
   search_fields= ['name']
   ordering_fields=['created_at']
   
   def get_queryset(self):
      return Product.objects.all()
   
   def get_permissions(self):
      if self.request.method=='POST':
         return [IsAuthenticated()]
      return [AllowAny()]

   
   def perform_create(self, serializer):
      if serializer.is_valid():
         serializer.save()
      else:
         return serializer.errors()
      



