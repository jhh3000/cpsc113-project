from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Presses(models.Model):
    time_stamp = models.TimeField()
    color = models.IntegerField #or boolean