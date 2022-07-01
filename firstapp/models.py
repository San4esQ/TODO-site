from django.db import models


class Users(models.Model):
    objects = models.Manager()

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Task(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
