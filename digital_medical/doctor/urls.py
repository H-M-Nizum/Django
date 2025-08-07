from django.urls import path
from .views import doctorViewAll, doctorInstanceView

urlpatterns = [
    path("list/", doctorViewAll, name='Doctor-List'),
    path("list/<int:pk>", doctorInstanceView, name='Doctor-Instance'),
]
