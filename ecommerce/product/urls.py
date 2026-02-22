from django.urls import path
from . import views

urlpatterns = [
    path('category/',views.CategoryListView.as_view()),
    path('category/<int:pk>/',views.CategoryView.as_view()),
    path('product/', views.ProductListView.as_view()),
    path('product/<int:pk>/',views.ProductDetailView.as_view()),


    ]