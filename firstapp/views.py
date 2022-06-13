import datetime

from django.shortcuts import render

from firstapp.models import Task


def index(request):
    tasks = Task.objects.all()

    result = []

    for task in tasks:
        result.append(task.title)

    return render(request, "index.html", context={"tasks": result})


def add(request):
    currentDate = datetime.datetime.now()

    return render(request, "add.html")
