from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(
            primary_key=True,
            editable=False,
            default=uuid.uuid4)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField()
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

