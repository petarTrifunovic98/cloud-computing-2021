from django.db import models

class Counter(models.Model):
    counter = models.PositiveIntegerField(null=False, default=0)
