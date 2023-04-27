from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    description = models.CharField(max_length=8000)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    def __str__(self):
        return self.title