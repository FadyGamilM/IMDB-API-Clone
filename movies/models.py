from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(blank=False, max_length=200)
    is_published = models.BooleanField(default=True)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name
