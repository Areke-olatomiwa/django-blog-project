from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    Title =models.CharField(max_length= 200)
    Text = models.TextField(default='input your text')
    Author = models.ForeignKey(User, on_delete= models.CASCADE)
    Created_date = models.DateTimeField(verbose_name=("Creation date"),auto_now_add=True, null=True)
    published_date = models.DateTimeField(verbose_name=("Creation date"),auto_now_add=True, null=True)