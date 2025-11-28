import pytest
from django.utils import timezone
from apps.blog.models import Post, Tag
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_post_creation():
    user = User.objects.create_user(username="author", password="1234", role="author")
    post = Post.objects.create(title="Test Post", content="Hello", author=user)
    assert post.title == "Test Post"
    assert post.status == "draft"

@pytest.mark.django_db
def test_post_publish_method():
    user = User.objects.create_user(username="author2", password="1234", role="author")
    post = Post.objects.create(title="Publish Me", content="Test", author=user)
    
    post.publish()
    post.refresh_from_db()

    assert post.status == "published"
    assert post.published_at is not None
