from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=CASCADE)

    def __str__(self) :
        return self.title
    def get_absolute_url(self): # new
        return reverse('post_detail' , args=[str(self.id)])