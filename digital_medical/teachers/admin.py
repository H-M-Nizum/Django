from django.contrib import admin
from .models import TeacherModel

# Register your models here.
@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "subject", "address", "join_date"]