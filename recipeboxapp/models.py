from django.db import models
from django.utils import timezone
# Create your models here.


class Author(...):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    byline = models.TextField()


class Article(...):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(...)
    time_created = models.DateTimeField(timezone.now)
