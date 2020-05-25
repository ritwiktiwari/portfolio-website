from django.db import models
from datetime import datetime

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project_url = models.URLField(max_length=500, blank=True)
    git_url = models.URLField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images/')
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
