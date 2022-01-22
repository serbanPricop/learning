from statistics import mode
from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Topic)
admin.site.register(models.WebPage)
admin.site.register(models.AccessRecord)
admin.site.register(models.UserProfileInfo)
