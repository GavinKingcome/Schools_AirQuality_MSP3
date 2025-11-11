from django.db import models

class School(models.Model):
    """Model representing a school"""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# Create your models here.