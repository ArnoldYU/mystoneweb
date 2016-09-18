# coding=utf-8
from django.db import models

# Create your models here.
class note(models.Model):
    theme=models.CharField(max_length=50)
    content=models.CharField(max_length=200)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    datetime=models.DateTimeField(auto_now_add=True)
