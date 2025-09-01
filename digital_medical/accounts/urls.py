from django.urls import path
from .views import UserRegistrationViews, UserLoginViews, UserProfileView, UserChangePasswordView, UserSendPasswordResetEmailView

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('login/', UserLoginViews.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', UserSendPasswordResetEmailView.as_view(), name='reset-password'),
]
