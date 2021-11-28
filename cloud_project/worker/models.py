from django.db import models

class Worker(models.Model):
    name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=False, max_length=70)
    date_of_birth = models.DateField(null=False)
    salary = models.DecimalField(null=False, max_digits=10, decimal_places=3)
