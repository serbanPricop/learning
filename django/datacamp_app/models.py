from pydoc_data.topics import topics
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
import datetime
from time import timezone


# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length = 50, unique = True)

    def __str__(self) -> str:
        return self.top_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.name)

    def was_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portofolio = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self) -> str:
        return self.user.username
