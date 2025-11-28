import pytest
from apps.accounts.models import User
from apps.blog.models import Post, Tag
from apps.comments.models import Comment

@pytest.mark.django_db
def test_user_roles():
    u = User.objects.create_user(username="reader", password="pw")
    assert u.role == "reader"
    a = User.objects.create_user(username="author", password="pw", role="author")
    assert a.is_author()

@pytest.mark.django_db
def test_post_and_tag():
    author = User.objects.create_user(username="a", password="pw", role="author")
    p = Post.objects.create(author=author, title="Title", content="Body")
    assert p.status == "draft"
    p.publish()
    p.refresh_from_db()
    assert p.status == "published"
    t = Tag.objects.create(name="django")
    p.tags.add(t)
    assert t in p.tags.all()

@pytest.mark.django_db
def test_comment_count_update():
    author = User.objects.create_user(username="a", password="pw", role="author")
    p = Post.objects.create(author=author, title="Title2", content="Body")
    c = Comment.objects.create(post=p, content="Nice", author=None)
    assert p.comments.count() == 1
