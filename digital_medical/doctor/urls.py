from django.urls import path
from .views import doctorViewAll, doctorInstanceView, createDoctorView, updateDoctorView

urlpatterns = [
    path("list/", doctorViewAll, name='Doctor-List'),
    path("list/<int:pk>", doctorInstanceView, name='Doctor-Instance'),
    path("create/", createDoctorView, name="Create-Doctor"),
    path("update/<int:pk>", updateDoctorView, name='Update-Doctor'),
]
