from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from firstapp.models import Task
from django.contrib.auth import authenticate
from .service import TaskService, AddService, EditService


def index(request):
    indexTask = TaskService.Index()

    result = indexTask.index(request)

    return render(request, "index.html", context={"tasks": result})


def add(request):
    addTask = AddService.Add()
    userTask = addTask.add(request)

    if request.method == "POST":
        if userTask.is_valid():

            return HttpResponseRedirect("/index")

    return render(request, "add.html", {"form": userTask})


def detail(request, num=1):
    task = Task.objects.get(id=num)
    return render(request, "detail.html", context={"data": task})


def edit(request, num=1):
    editTask = EditService.Edit()
    change = editTask.edit(request, num)

    if request.method == "POST":
        return HttpResponseRedirect("/index")

    return render(request, "edit.html", context={"edit": change})


def delete(request, num=1):
    task = Task.objects.get(id=num)
    task.delete()

    return HttpResponseRedirect("/index")


@csrf_exempt
def register(request):
    result = {'form': UserCreationForm()}

    if request.POST:
        newUser = UserCreationForm(request.POST)

        if newUser.is_valid():
            newUser.save()
            newUser = auth.authenticate(username=newUser.cleaned_data['username'],
                                        password=newUser.cleaned_data['password2'])
            auth.login(requset, newUser)
            return HttpResponseRedirect('/')

        else:
            result['form'] = newUser
    return render(request, 'register.html', result)


@csrf_exempt
def entry(request):
    result = {}

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/index')

        else:
            login_error = "Пользователь не найден"
            return render(request, 'entry.html', {'login_error': login_error})

    else:
        return render(request, "entry.html", result)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
