from django.shortcuts import render
from .models import ProductModel
from .serializers import ProductSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.

class ProductListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ProductDetailsVIew(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)