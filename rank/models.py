from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Rank(models.Model):
    def __unicode__(self):
        return 'Username: ' + self.username
    username = models.CharField(max_length=200)
    facebook_id = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    points = models.CharField(max_length=200)
    highest_score = models.CharField(max_length=200)

