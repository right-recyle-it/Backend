from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

# class Donate(models.Model):
#     name = models.CharField(max_length=10, null=True, blank=True)
#     kind = models.CharField(max_length=30, null=True, blank=True)
#     condition = models.CharField(max_length=10, null=True, blank=True)
#     upgrade = models.CharField(max_length=2, null=True, blank=True)
#     last_update = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
