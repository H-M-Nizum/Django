from django.urls import path
from .views import ProductListCreateView, ProductDetailsVIew

urlpatterns = [
    path("product/", ProductListCreateView.as_view(), name='product-mixin-list'),
    path("product/<int:pk>", ProductDetailsVIew.as_view(), name='product-mixin-instance')
]
