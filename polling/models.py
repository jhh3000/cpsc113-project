from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
	time_stamp = models.TimeField()
	understand = models.BooleanField()
	user = models.ForeignKey(User)
