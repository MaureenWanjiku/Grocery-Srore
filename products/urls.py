from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.index),
    path('new', views.new),
    path('product_details/<int:id>', views.product_details),
    path('add-to-cart/<int:product_id>/', views.add_to_cart),
]