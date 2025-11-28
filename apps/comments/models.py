from django.db import models
from django.conf import settings
from apps.blog.models import Post

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)  # auto-approval for MVP

    class Meta:
        ordering = ("created_at",)
