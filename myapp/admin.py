from django.contrib import admin
from .models import Book, BookImage

admin.site.register(Book)
admin.site.register(BookImage)