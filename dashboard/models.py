from django.db import models

# Create your models here.

class ElectricVichele(models.Model):
    make=models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    electric_range = models.FloatField()
    vichele_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
