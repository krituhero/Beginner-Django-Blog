from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)


class Post(models.Model):
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} - {self.title}"




"""class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')"""


class blogcomment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE),
    text = models.TextField()

    def str(self):
        return self.name



class Orders(models.Model):
    pass