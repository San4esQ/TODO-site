from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from firstapp.models import Task, Users

from .forms import UserTask, UserLogin

from django.contrib.auth import authenticate


# тест auth

def test(requset):
    user = authenticate(username='root', password='1234')
    if user is not None:
        return HttpResponseRedirect('/index')
    else:
        return HttpResponse('NO')





def preview(request):
    return render(request, "preview.html")


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

            # беру id из внешнего ключа
            newUser = Users.objects.get(id=17)

            # добавление новой задачи даты и время
            newTask = Task.objects.update_or_create(defaults=value_for_update, id=None, user=newUser)
            return HttpResponseRedirect("/index")

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
        return HttpResponseRedirect("/index")
    return render(request, "edit.html", context={"edit": task})


def delete(request, num=1):
    task = Task.objects.get(id=num)
    task.delete()

    return HttpResponseRedirect("/index")


def register(requset):
    users = UserLogin()
    if requset.method == "POST":
        users = UserLogin(requset.POST)
        if users.is_valid():
            usernameAdd = users.cleaned_data['usernameAdd']
            passwordAdd = users.cleaned_data['passwordAdd']
            value_for_update = {"username": usernameAdd, "password": passwordAdd}

            # добавление нового пользователя в БД
            newUser = Users.objects.update_or_create(defaults=value_for_update, id=None)
            return HttpResponseRedirect("/index")
    return render(requset, "register.html", {"register": users})


def entry(request):
    if request.method == "POST":
        # Получаем с фронта данные на бэк
        login = request.POST.get('login')
        password = request.POST.get('password')

        try:
            user = Users.objects.get(username=login, password=password)
            return HttpResponseRedirect('/index')
        # если данных в БД нет то редирект на вход
        except BaseException:
            return HttpResponseRedirect('/entry')

    return render(request, "entry.html")
