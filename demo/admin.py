from django.contrib import admin
from .models import Book, BookNumber

## registering class with decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['title', 'price']
	list_filter = ['price']
	search_fields = ['title']

admin.site.register(BookNumber)