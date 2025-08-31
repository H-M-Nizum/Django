from django.urls import path
from .views import UserRegistrationViews, UserLoginViews, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('login/', UserLoginViews.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
