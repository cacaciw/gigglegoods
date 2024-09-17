from django.db import models
import uuid

# Create your models here.
class GiggleCatalogue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    giggleLevel = models.IntegerField()
    time = models.DateField(auto_now_add=True)

