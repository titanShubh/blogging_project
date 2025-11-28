import pytest
from apps.blog.models import Post
from apps.comments.models import Comment
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_comment():
    user = User.objects.create_user(username="reader", password="123")
    post = Post.objects.create(title="Comment Test", content="Hi", author=user)
    
    comment = Comment.objects.create(post=post, author=user, content="Nice post!")
    
    assert comment.content == "Nice post!"
    assert comment.post == post

@pytest.mark.django_db
def test_comment_auto_approved():
    user = User.objects.create_user(username="reader2", password="123")
    post = Post.objects.create(title="Test2", content="Hi", author=user)

    comment = Comment.objects.create(post=post, author=user, content="Approved?")
    
    assert comment.approved is True
