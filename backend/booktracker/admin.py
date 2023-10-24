from django.contrib import admin
from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'read', 'author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'lastname')

admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)
