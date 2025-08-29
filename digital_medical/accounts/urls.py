from django.urls import path
from .views import UserRegistrationViews, UserLoginViews

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('login/', UserLoginViews.as_view(), name='login'),
]
