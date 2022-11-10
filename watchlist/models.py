from django.db import models

# Create your models here.
class WatchList(models.Model):
    """Model representing a WatchList"""
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title()
    

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    