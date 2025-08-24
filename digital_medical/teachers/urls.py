from django.urls import path
from .views import TeacherListCreateView, TeacherRetriveUpdateDestroyView, TeacherRetriveDestroyView, TeacherRetriveUpdateView

urlpatterns = [
    path('teacher/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teacher/<int:pk>', TeacherRetriveUpdateDestroyView.as_view(), name='teacher-retrive-update-destroy'),
    path('teacher/retrive-destroy/<int:pk>', TeacherRetriveDestroyView.as_view(), name='teacher-retrive-destroy'),
    path('teacher/retrive-update/<int:pk>', TeacherRetriveUpdateView.as_view(), name='teacher-retrive-update'),
    
]
