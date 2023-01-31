from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=255, unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self) -> str:
        return "{}".format(self.name)

    class Meta:
        ordering = ('-name',)