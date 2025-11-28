from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models
from .models import Like
from apps.blog.models import Post

@receiver(post_delete, sender=Like)
def on_like_deleted(sender, instance, **kwargs):
    Post.objects.filter(id=instance.post_id).update(likes_count=models.F("likes_count") - 1)
