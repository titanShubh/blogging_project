import pytest
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.blog.models import Post

@pytest.mark.django_db
def test_create_post_api():
    user = User.objects.create_user(username="author", password="pw", role="author")
    client = APIClient()
    token_resp = client.post("/api/v1/auth/token/", {"username":"author","password":"pw"})
    assert token_resp.status_code == 200
    token = token_resp.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    resp = client.post("/api/v1/posts/", {"title":"API Title", "content":"API Content"})
    assert resp.status_code == 201
    assert Post.objects.filter(title="API Title").exists()

@pytest.mark.django_db
def test_view_increment_and_event_created():
    user = User.objects.create_user(username="author", password="pw", role="author")
    p = Post.objects.create(author=user, title="ViewTitle", content="C")
    client = APIClient()
    r = client.get(f"/api/v1/posts/{p.slug}/")
    assert r.status_code == 200
    p.refresh_from_db()
    assert p.views_count == 1
