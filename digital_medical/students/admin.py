from django.contrib import admin
from .models import StudentModel

# Register your models here.
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'roll', 'age', 'address', 'class_name']
