from django.db import models

# Create your models here.
class FilterDemo(models.Model):
    name=models.CharField(max_length=30)
    subjects=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    date=models.DateField()
