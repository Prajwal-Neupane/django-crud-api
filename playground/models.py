from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

# Create your models here.
