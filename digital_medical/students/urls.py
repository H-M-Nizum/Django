from django.urls import path
from .views import StudentsApiView

urlpatterns = [
   path('student/', StudentsApiView.as_view(), name='student-api-list'),
   path('student/<int:pk>', StudentsApiView.as_view(), name='student-api-instance'),
]
