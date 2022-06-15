
from django.shortcuts import render

from firstapp.models import Task

from .forms import UserTask


def index(request):
    tasks = Task.objects.all()

    result = {}

    for task in tasks:
        result[task.date] = task.title

    return render(request, "index.html", context={"tasks": result})


def add(request):
    userTask = UserTask()
    if request.method == "POST":
        userTask = UserTask(request.POST)
        if userTask.is_valid():
            dateAdd = userTask.cleaned_data["dateAdd"]
            timeAdd = userTask.cleaned_data["timeAdd"]
            taskAdd = userTask.cleaned_data["taskAdd"]
            #return HttpResponse("<h2>Задача '{0}', добавлена на дату {2} в {1} часов".format(taskAdd, timeAdd, dateAdd))
            value_for_update = {"title": taskAdd, "date": dateAdd, "time": timeAdd} #значения для добавления взятые выше
            newTask = Task.objects.update_or_create(defaults=value_for_update, id=None)#добавление новой задачи даты и время
    return render(request, "add.html", {"form": userTask})