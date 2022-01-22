import datetime
from time import time
from django.db import models
from django.utils import timezone

# Create your models here.

class Bicyle(models.Model):
    created = models.DateTimeField(default=timezone.now())
    name = models.CharField(max_length=50)
    reason = models.CharField(max_length=256)
    estimed_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(7))

    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return self.name