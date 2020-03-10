from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Resorts(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

# Create your models here.
class Tours(models.Model):
    country = models.ForeignKey(Countries, on_delete=None, default=None)
    resort = models.ForeignKey(Resorts, on_delete=None, null=True, default=None)

