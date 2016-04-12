from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Presses(models.Model):
	time_stamp = models.TimeField()
	color = models.BooleanField()