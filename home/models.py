from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=280)
    slug = models.SlugField(max_length=280, unique=True)
    date_created = models.DateField()


