import pytest
from apps.blog.models import Tag

@pytest.mark.django_db
def test_tag_creation():
    tag = Tag.objects.create(name="Django")
    assert tag.name == "Django"

@pytest.mark.django_db
def test_tag_slug_auto_generation():
    tag = Tag.objects.create(name="Hello World")
    assert tag.slug == "hello-world"
