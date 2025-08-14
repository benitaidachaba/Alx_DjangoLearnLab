from django.contrib import admin
from .models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "department")
    search_fields = ("name", "department")

admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)