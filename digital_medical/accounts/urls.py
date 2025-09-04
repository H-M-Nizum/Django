from django.urls import path
from .views import UserRegistrationViews, UserLoginViews, UserProfileView, UserChangePasswordView, UserSendPasswordResetEmailView, UserPasswordResetView, UserLogoutView

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('login/', UserLoginViews.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('send-reset-password-mail/', UserSendPasswordResetEmailView.as_view(), name='send-reset-password-mail'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]
