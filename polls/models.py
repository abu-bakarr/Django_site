from datetime import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    tittle = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '{}'.format(self.tittle)

    class Meta:
        verbose_name_plural = 'Posts'
