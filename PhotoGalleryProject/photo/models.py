from __future__ import unicode_literals

from django.db import models

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Photography(models.Model):
    class Meta():
        db_table = "photography"
    photo = models.ImageField(upload_to=upload_location)