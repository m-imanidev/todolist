from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response 
from rest_framework import status

from .serializers import TodoListSerializer, ItemListSerializer, TagSerializer, CommentSerializer
from .models import TodoList, TodoItem, Tag, Comment

@method_decorator(cache_page(1 * 60), name='dispatch')
class TodoListViews(ListCreateAPIView):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.filter(is_active=True)

class SingleTodoListViews(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoListSerializer
    import time
    time.sleep(10)
    print("hiii----------------")
    queryset = TodoList.objects.all()
    lookup_field = 'pk'


class ItemListViews(ListCreateAPIView):
    serializer_class = ItemListSerializer

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list_id=self.kwargs["pk"])

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
        
    def perform_create(self, serializer):
        todo_list = self.kwargs.get("pk")
        serializer.save(todo_list_id=todo_list, created_by=self.request.user)

class SingleItemListViews(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemListSerializer
    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    lookup_field = 'id'
    def put(self, request, *args, **kwargs):
        user = self.request.user
        print("User is: ", self.request.user)
        assign_item = TodoItem.objects.get(id=self.kwargs["id"]).assign.all()
        if user in assign_item:
            return self.update(request, *args, **kwargs)
        else:
            return Response({"detail": "You do not have access to change."},status= status.HTTP_401_UNAUTHORIZED)
    


class CommentListViews(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

        
class SingleCommentViews(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
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
