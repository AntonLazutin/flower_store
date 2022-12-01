from django.db import models



class Flower(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name