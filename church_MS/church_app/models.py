from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title