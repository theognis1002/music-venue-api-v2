from django.db import models


# Create your models here.
class Venue(models.Model):
    venue = models.CharField(max_length=255)
    capacity = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=10)

    def __str__(self):
        return self.venue