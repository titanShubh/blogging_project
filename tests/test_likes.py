import pytest
from apps.blog.models import Post
from apps.interactions.models import Like
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_like_creation():
    user = User.objects.create_user(username="likeuser", password="123")
    post = Post.objects.create(title="Like Post", content="test", author=user)

    like = Like.objects.create(user=user, post=post)
    assert like.post == post
    assert like.user == user

@pytest.mark.django_db
def test_prevent_duplicate_like():
    user = User.objects.create_user(username="likeuser2", password="123")
    post = Post.objects.create(title="Double Like", content="test", author=user)

    Like.objects.create(user=user, post=post)

    with pytest.raises(Exception):
        Like.objects.create(user=user, post=post)  # violates unique constraint
