from django.contrib import admin

# Register your models here.
from .models import Task


class taskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'manager']
    search_fields = ['name']
    list_filter = ['status']

admin.site.register(Task,taskAdmin)