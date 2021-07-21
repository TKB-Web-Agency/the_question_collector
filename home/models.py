from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=280)
    slug = models.SlugField(max_length=280, unique=True)

    def __str__(self):
        return (self.title)

class Question(models.Model):
    title = models.CharField(max_length=280)
    slug = models.SlugField(max_length=280, unique=True)
    date_created = models.DateField()
    categories = models.ManyToManyField(Categories, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, default='')
    
