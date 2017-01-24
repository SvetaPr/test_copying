from __future__ import unicode_literals

from django.db import models

class Photography(models.Model):
    class Meta():
        db_table = "photography"
    photo_title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='%Y_%m_%d/')
    photo_date = models.DateTimeField()

