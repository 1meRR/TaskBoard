from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'assignee', 'created_at')
    list_filter = ('status', 'assignee')
    search_fields = ('title', 'description')
