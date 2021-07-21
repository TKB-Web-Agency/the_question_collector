from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
        website = models.URLField(max_length=200, blank=True)
        github = models.URLField(max_length=200, blank=True)
        picture = models.URLField(max_length=200, blank=True)
        about = models.TextField(blank=True)
        uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
