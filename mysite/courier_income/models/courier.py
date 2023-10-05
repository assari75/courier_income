from django.db import models


class Courier(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Courier"
        verbose_name_plural = "Couriers"
    
    def __str__(self):
        return self.name
