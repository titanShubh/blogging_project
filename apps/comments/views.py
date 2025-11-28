from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_pk = self.kwargs.get("post_pk")
        return Comment.objects.filter(post__pk=post_pk)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
