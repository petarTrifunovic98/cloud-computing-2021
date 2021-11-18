from django.db import models

class Zaposleni(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    salary = models.FloatField()
