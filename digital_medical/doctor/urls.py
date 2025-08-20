from django.urls import path
from .views import doctorViewAll, doctorInstanceView, createDoctorView

urlpatterns = [
    path("list/", doctorViewAll, name='Doctor-List'),
    path("list/<int:pk>", doctorInstanceView, name='Doctor-Instance'),
    path("create/", createDoctorView, name="create_doctor")
]
