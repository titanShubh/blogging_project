from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction, models
from .models import Post, Tag
from .serializers import PostListSerializer, PostDetailSerializer, TagSerializer

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user.is_admin() or obj.author_id == request.user.id)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related("author").prefetch_related("tags")
    lookup_field = "slug"
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("status", "author__username", "tags__slug")
    search_fields = ("title", "content", "excerpt", "tags__name")

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy", "publish"):
            return [permissions.IsAuthenticated(),]
        return [permissions.AllowAny()]

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def publish(self, request, slug=None):
        post = self.get_object()
        if not request.user.is_author() and not request.user.is_admin():
            return Response({"detail": "Not permitted"}, status=status.HTTP_403_FORBIDDEN)
        post.publish()
        return Response({"status": "published"})
    
    def retrieve(self, request, *args, **kwargs):
        # increment views atomically
        instance = self.get_object()
        Post.objects.filter(pk=instance.pk).update(views_count=models.F("views_count") + 1)
        # create analytics event - import lazily to avoid circular import
        from apps.analytics.models import Event
        Event.objects.create(user=request.user if request.user.is_authenticated else None, post=instance, event_type="view")
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
