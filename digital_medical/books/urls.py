from django.urls import path
from .views import booksApiView

urlpatterns = [
    path("book/", booksApiView, name="books"),
    path("book/<int:pk>", booksApiView, name="book"),
]
