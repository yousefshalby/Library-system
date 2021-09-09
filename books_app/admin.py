from django.contrib import admin
from books_app import models
from .models import Books, Category
# Register your models here.

admin.site.register(Books)
admin.site.register(Category)