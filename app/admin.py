from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'author', 'is_complete', 'shelf_number')



admin.site.register(Book, BookAdmin)
