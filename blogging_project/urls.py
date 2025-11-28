from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.blog.views import PostViewSet, TagViewSet
from apps.comments.views import CommentViewSet
from apps.interactions.views import LikeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("tags", TagViewSet, basename="tags")
router.register(r"posts/(?P<post_pk>[^/.]+)/comments", CommentViewSet, basename="post-comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
