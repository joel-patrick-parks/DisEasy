from __future__ import unicode_literals

from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.
class TrainedModel(models.Model):
    model = PickledObjectField(default=None)
    diseaseState = models.CharField(max_length=100, null=False, db_index=True);

    # for normalizing inputs - store lists of floats
    medians = PickledObjectField()
    standardDeviations = PickledObjectField()

    accuracy = models.FloatField()
