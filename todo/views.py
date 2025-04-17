from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView

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
        todo_list = self.kwargs.get("pk")
        return TodoItem.objects.filter(todo_list_id=todo_list) 
class SingleItemListViews(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemListSerializer
    queryset = TodoItem.objects.all()
    lookup_field = 'id'


class CommentListViews(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
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
