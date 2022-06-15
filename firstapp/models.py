from django.db import models


class Task(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
