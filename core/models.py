from django.db import models


class Footballer(models.Model):
    name = models.CharField(max_length=255)
    number = models.SmallIntegerField()

    def __str__(self):
        return self.name
