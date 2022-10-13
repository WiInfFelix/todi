from django.conf import settings
from django.db import models

class Project(models.Model):

    name = models.CharField(max_length=256)

    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
