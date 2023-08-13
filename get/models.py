from django.db import models

# Create your models here.

class Get(models.Model):
    name = models.CharField(max_length=10, primary_key= True)
    kind = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    reason = models.CharField(max_length = 100)
    last_update = models.DateField()

    def __str__(self):
        return self.kind