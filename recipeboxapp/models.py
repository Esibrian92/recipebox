from django.db import models
from django.utils import timezone
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    time_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
