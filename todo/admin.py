from django.contrib import admin

from .models import Comment, TodoList

@admin.register(TodoList)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("name", "is_active")}),)
