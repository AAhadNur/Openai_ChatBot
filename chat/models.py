from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Conversation(models.Model):
    user = models.ForeignKey(
        User, related_name="conversations", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Chat(models.Model):
    user = models.ForeignKey(User, related_name="chats",
                             on_delete=models.CASCADE)
    topic = models.ForeignKey(
        Conversation, related_name="chats", on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
