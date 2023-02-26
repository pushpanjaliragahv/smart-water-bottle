from django.db import models

# Create your models here.
from django.db import models

class Detail(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    weight = models.CharField(max_length=100)

    def __str__(self):
        return self.name