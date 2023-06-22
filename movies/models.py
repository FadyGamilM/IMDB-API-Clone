from django.db import models

# Create your models here.


class Content(models.Model):
    name = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    website = models.URLField()

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name