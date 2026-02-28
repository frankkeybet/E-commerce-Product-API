from rest_framework import serializers
from .models import Product ,Category
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','username','password','email','is_staff']
        extra_kwargs= {"password":{"write_only":True}}
    def create(self,validated_data):
        user= User.objects.create_user(**validated_data)
        return user

class ResetPassword(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self , value):
        validate_password(value)
        return value