from django.urls import path, include
from .views import TeacherListCreateView, TeacherRetriveUpdateDestroyView, TeacherRetriveDestroyView, TeacherRetriveUpdateView, TeacherModelViewSetView
from rest_framework.routers import DefaultRouter

# Router for ModelViewSet
router = DefaultRouter()
router.register('teacher-viewset', TeacherModelViewSetView, basename='teacher')


urlpatterns = [
    # Old class-based APIViews
    path('teacher/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teacher/<int:pk>', TeacherRetriveUpdateDestroyView.as_view(), name='teacher-retrive-update-destroy'),
    path('teacher/retrive-destroy/<int:pk>', TeacherRetriveDestroyView.as_view(), name='teacher-retrive-destroy'),
    path('teacher/retrive-update/<int:pk>', TeacherRetriveUpdateView.as_view(), name='teacher-retrive-update'),
    

    # ModelViewSet routes
    path('', include(router.urls)),
]
