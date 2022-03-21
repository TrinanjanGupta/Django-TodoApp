from tkinter import CASCADE
from unicodedata import name
from click import progressbar
from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
    
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    is_status = models.ForeignKey(Status,on_delete=models.CASCADE, null=True,)
    
    def __str__(self):
        return self.title
    
    
    
