from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from firstapp.models import Task
from .forms import UserTask
from django.contrib.auth import authenticate


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
            return HttpResponseRedirect("/")

    return render(request, "add.html", {"form": userTask})


def detail(request, num=1):
    task = Task.objects.get(id=num)
    return render(request, "detail.html", context={"data": task})


def edit(request, num=1):
    task = Task.objects.get(id=num)
    if request.method == "POST":
        task.date = request.POST.get("date")
        task.time = request.POST.get("time")
        task.title = request.POST.get("title")
        task.save()
        return HttpResponseRedirect("/")
    return render(request, "edit.html", context={"edit": task})


def delete(request, num=1):
    task = Task.objects.get(id=num)
    task.delete()

    return HttpResponseRedirect("/")


@csrf_exempt
def register(requset):
    result = {'form': UserCreationForm()}
    if requset.POST:
        newUser = UserCreationForm(requset.POST)
        if newUser.is_valid():
            newUser.save()
            newUser = auth.authenticate(username=newUser.cleaned_data['username'],
                                        password=newUser.cleaned_data['password2'])
            auth.login(requset, newUser)
            return HttpResponseRedirect('/')
        else:
            result['form'] = newUser
    return render(requset, 'register.html', result)


@csrf_exempt
def entry(request):
    result = {}

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html', {'username': username})

        else:
            login_error = "Пользователь не найден"
            return render(request, 'entry.html', {'login_error': login_error})

    else:
        return render(request, "entry.html", result)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
