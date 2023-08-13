from django.db import models

# Create your models here.

class Donate(models.Model):
    name = models.CharField(max_length=10, primary_key= True)
    kind = models.CharField(max_length=30)
    condition = models.CharField(max_length=10)
    upgrade = models.CharField(max_length = 2)
    last_update = models.DateField()

    def __str__(self):
        return self.kind