from django.urls import path
from .views import homeView, aboutView, servicesView, contactView

urlpatterns = [
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('services/', servicesView, name='services'),
    path('contact/', contactView, name='contact'),
]
