from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response 
from rest_framework import status
from .serializers import TodoListSerializer, ItemListSerializer, TagSerializer, CommentSerializer
from .models import TodoList, TodoItem, Tag, Comment

class TodoListViews(ListCreateAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.filter(is_active=True)

class SingleTodoListViews(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    lookup_field = 'pk'



class ItemListViews(ListCreateAPIView):
    serializer_class = ItemListSerializer

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        todo_list = self.kwargs.get("pk")
        serializer.save(todo_list_id=todo_list)

class SingleItemListViews(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemListSerializer
    queryset = TodoItem.objects.all()
    lookup_field = 'id'


class CommentListViews(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

        
class SingleCommentViews(RetrieveUpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = "pk"


class SingleTagViews(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = "pk"
class TagListViews(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
