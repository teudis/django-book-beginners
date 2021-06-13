from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=CASCADE)

    def __str__(self) :
        return self.title