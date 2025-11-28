from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from apps.blog.models import Post
from django.db import transaction, models

class LikeView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = request.data.get("post")
        if not post_id:
            return Response({"detail": "post is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "post not found"}, status=status.HTTP_404_NOT_FOUND)
        # create like only if not exists
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Post.objects.filter(pk=post.pk).update(likes_count=models.F("likes_count") + 1)
            # create analytics event
            from apps.analytics.models import Event
            Event.objects.create(user=request.user, post=post, event_type="like")
            return Response({"status": "liked"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "already liked"}, status=status.HTTP_200_OK)
