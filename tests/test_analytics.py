import pytest
from apps.blog.models import Post
from apps.analytics.models import Event
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_event_logging():
    user = User.objects.create_user(username="loguser", password="123")
    post = Post.objects.create(title="Event Post", content="Log", author=user)

    event = Event.objects.create(user=user, post=post, event_type="view")

    assert event.event_type == "view"
    assert event.post == post

@pytest.mark.django_db
def test_multiple_events():
    user = User.objects.create_user(username="multi", password="123")
    post = Post.objects.create(title="Multi Event Post", content="Log", author=user)

    Event.objects.create(user=user, post=post, event_type="view")
    Event.objects.create(user=user, post=post, event_type="like")

    assert Event.objects.filter(post=post).count() == 2
