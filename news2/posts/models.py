from django.db import models
from django.db.models.fields import CharField

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()