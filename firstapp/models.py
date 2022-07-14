from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
