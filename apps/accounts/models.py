from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_ADMIN = "admin"
    ROLE_AUTHOR = "author"
    ROLE_READER = "reader"

    ROLE_CHOICES = (
        (ROLE_ADMIN, "Admin"),
        (ROLE_AUTHOR, "Author"),
        (ROLE_READER, "Reader"),
    )

    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default=ROLE_READER)

    def is_admin(self):
        return self.role == self.ROLE_ADMIN or self.is_superuser

    def is_author(self):
        return self.role == self.ROLE_AUTHOR or self.is_superuser
