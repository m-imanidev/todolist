from django.urls import path

from .views import (TodoListViews, SingleTodoListViews,
                    ItemListViews, SingleItemListViews,
                    SingleTagViews, TagListViews, CommentListViews,
                    SingleCommentViews
                    )

urlpatterns = [
    path('lists/', TodoListViews.as_view(), name='todo-lists'),
    path('lists/<int:pk>', SingleTodoListViews.as_view()),
    
    path('lists/<int:pk>/items', ItemListViews.as_view()),
    path('items/<int:id>', SingleItemListViews.as_view()),
    path('comments/', CommentListViews.as_view()),
    path('comments/<int:pk>', SingleCommentViews.as_view()),

    path('tags/<int:pk>', SingleTagViews.as_view()),
    path('tags/', TagListViews.as_view()),
]
