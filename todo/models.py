from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def items_count(self):
        return self.items.count()
    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["title"]
    def __str__(self):
        return self.title


class TodoItem(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    status = models.CharField(choices=Status.choices, default=Status.PENDING)
    assign = models.ManyToManyField(User, related_name="assigned_comments", blank=True)
    tags = models.ManyToManyField(Tag)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    class Status(models.TextChoices):
        NEED_TO_CHECK = 'need_to_check', 'Need to check'
        NOT_CONFIRMED = 'not_confirmed', 'Not confirmed'
        CONFIRMED = 'confirmed', 'Confirmed'

    todo_item = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    body = models.TextField()
    status = models.CharField(choices=Status.choices, default=Status.NEED_TO_CHECK)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

