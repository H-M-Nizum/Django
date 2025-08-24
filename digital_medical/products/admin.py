from django.contrib import admin
from .models import ProductModel

# Register your models here.
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "oum", "price", "stock", "exp_date"]