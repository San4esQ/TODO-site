from django.db import models


class Task(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()


class Users(models.Model):
    objects = models.Manager()

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
