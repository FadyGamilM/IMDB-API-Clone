from django.db import models

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class StreamingPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    website = models.URLField()
    # one platform can stream multiple tv contents

    def __str__(self) -> str:
        return self.name


class Content(models.Model):
    name = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    streaming_platform = models.ForeignKey(
        StreamingPlatform,
        on_delete=models.CASCADE,
        # the related_name is used when we work with the reverse side of the relation
        related_name='content'
    )

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # user can rate the content without typing a text review
    description = models.TextField(null=True)
    # get set on the creation time only
    created_at = models.DateTimeField(auto_now_add=True)
    # get updated each time we call the save method in this object
    updated_at = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self):
        # return rating not desc because desc might be null at some reviews
        return str(self.rating)
