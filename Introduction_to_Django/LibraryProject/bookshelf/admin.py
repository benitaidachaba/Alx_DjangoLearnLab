from django.contrib import admin
from .models import Book


class Bookadmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)


# Register your models here.
admin.site.register(Book, Bookadmin)
