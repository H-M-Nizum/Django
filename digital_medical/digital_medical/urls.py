from django.contrib import admin
from django.urls import path, include

# For Simple jwt Configuration
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # For Simple jwt Configuration
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('doctor/', include('doctor.urls')),
    path('books/', include('books.urls')),
    path('students/', include('students.urls')),
    path('products/', include('products.urls')),
    path('teachers/', include('teachers.urls')),
    path('api/auth/', include('accounts.urls'))
]
