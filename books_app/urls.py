from django.urls import path
from books_app import views
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.books, name='books'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]