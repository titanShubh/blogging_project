import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(username="testuser", password="testpass", role="reader")
    assert user.username == "testuser"
    assert user.check_password("testpass")

@pytest.mark.django_db
def test_user_role_assignment():
    user = User.objects.create_user(username="author", password="pass123", role="author")
    assert user.role == "author"
    assert user.is_author()
