from django.db import models

from django.db import models

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
        on_delete= models.CASCADE,
        related_name='content' # the related_name is used when we work with the reverse side of the relation
    )

    def __str__(self) -> str:
        return self.name
    