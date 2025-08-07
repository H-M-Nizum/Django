from django.contrib import admin
from . models import DoctorModel

# Register your models here.
@admin.register(DoctorModel)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation', 'email', 'phone', 'age', 'created_at', 'updated_at']
