from django.db import models

# Create your models here.
class GiggleCatalogue(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    giggleLevel = models.IntegerField()

    