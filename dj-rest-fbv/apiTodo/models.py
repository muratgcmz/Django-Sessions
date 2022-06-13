from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField()
    TİTLE = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )


    priority = models.CharField(max_length=50, choices=TİTLE, default='L')
    done = models.BooleanField()
    updateDate = models.DateTimeField(auto_now=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task