from rest_framework import serializers

from .models import TodoList, TodoItem, Tag, Comment

class ItemListSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    comments = serializers.SerializerMethodField(read_only=True)
    todo_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = TodoItem
        fields = ["id", "title", "status", "todo_list", "body", "tags", "comments"]
    def get_comments(self, obj):
        related_comments = Comment.objects.filter(todo_item=obj)
        return CommentSerializer(related_comments, many=True).data
    def get_todo_list(self, obj):
        todolist = obj.todo_list
        return {"id": todolist.id, "name": todolist.name}


class TodoListSerializer(serializers.ModelSerializer):
    items_counts = serializers.SerializerMethodField(read_only=True)
    items = ItemListSerializer(many=True, read_only=True)
    class Meta:
        model = TodoList
        fields = ["id", "name", "items_counts", "items"]
    
    def get_items_counts(self, obj: TodoList):
        return obj.items_count


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["status", "todo_item", "body"]

class TagSerializer(serializers.ModelSerializer):
    todo_item = ItemListSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = ["title", "todo_item"]
