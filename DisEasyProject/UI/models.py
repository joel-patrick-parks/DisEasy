from __future__ import unicode_literals

from django.db import models

class Visualization(models.Model):
    json = models.TextField()
    test = models.CharField(max_length = 50, default="none", db_index=True)
    group = models.CharField(max_length = 50, default="none", db_index=True)
