from django.db import models

# Create your models here.


class Donate(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    # kind = models.CharField(max_length=30, null=True, blank=True)
    condition = models.CharField(max_length=10, null=True, blank=True)
    upgrade = models.CharField(max_length=2, null=True, blank=True)
    # last_update = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.kind
