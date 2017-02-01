from __future__ import unicode_literals

from django.db import models

class Visualization(models.Model):
    IV = models.CharField(max_length = 30, null=True)
    FeatureType = models.CharField(max_length = 30, null=True, db_index=True)
    FeatureValue = models.CharField(max_length = 30, null=True, db_index=True)
    Data = models.TextField(null=True)
    UserResult = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    UserProbability = models.DecimalField(max_digits=6, decimal_places=3, default=0)

    def as_json(self):
        return dict(
                IV=str(self.IV),
                Feature=dict(
                    Type=str(self.FeatureType),
                    Value=str(self.FeatureValue),
                    ),
                Data=map(lambda x: map (lambda y: float(y), x.split(",")), self.Data.split("|")),
                User=dict(
                    result=float(self.UserResult),
                    probability=float(self.UserProbability),
                    )
                )
