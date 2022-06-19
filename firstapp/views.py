from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from firstapp.models import Task

from .forms import UserTask


def index(request):
    tasks = Task.objects.all()

    result = {}

    for task in tasks:
        key = task.date

        result.setdefault(key, []).append(task)

    return render(request, "index.html", context={"tasks": result})


def add(request):
    userTask = UserTask()

    if request.method == "POST":
        userTask = UserTask(request.POST)
        if userTask.is_valid():
            dateAdd = userTask.cleaned_data["dateAdd"]
            timeAdd = userTask.cleaned_data["timeAdd"]
            taskAdd = userTask.cleaned_data["taskAdd"]

            # значения для добавления взятые выше
            value_for_update = {"title": taskAdd, "date": dateAdd, "time": timeAdd}

            # добавление новой задачи даты и время
            newTask = Task.objects.update_or_create(defaults=value_for_update, id=None)
            return HttpResponseRedirect("/index")

    return render(request, "add.html", {"form": userTask})

def view(request, num = 1):
    task = Task.objects.get(id = num)
    return render(request, "detail.html", context={"data": task})

def edit(request, num = 1):
    task = Task.objects.get(id = num)
    if request.method == "POST":
        task.date = request.POST.get("date")
        task.time = request.POST.get("time")
        task.title = request.POST.get("title")
        task.save()
        return HttpResponseRedirect("/index")
    return render(request, "edit.html", context={"edit": task})
