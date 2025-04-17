from rest_framework import serializers

from .models import TodoList, TodoItem, Tag, Comment

class ItemListSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    comments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = TodoItem
        fields = ["id", "title", "status", "todo_list", "body", "tags", "comments"]
    def get_comments(self, obj):
        related_comments = Comment.objects.filter(todo_item=obj)
        return CommentSerializer(related_comments, many=True).data


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
        fields = ["title", "status", "todo_item", "body"]

class TagSerializer(serializers.ModelSerializer):
    todo_item = ItemListSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = ["title", "todo_item"]
