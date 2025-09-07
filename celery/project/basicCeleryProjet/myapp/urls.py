from django.urls import path
from .views import homeView, aboutView, servicesView, contactView, displayTaskView, get_task_result

urlpatterns = [
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('services/', servicesView, name='services'),
    path('contact/', contactView, name='contact'),
    path('display-task-result/', displayTaskView, name='display-task-result'),
    path('get-task-result/<str:task_id>/', get_task_result, name='get-task-result')
]
