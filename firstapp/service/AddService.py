from firstapp.forms import UserTask
from firstapp.models import Task


class Add:
    def add(self, request):
        userTask = UserTask()

        if request.method == "POST":
            userTask = UserTask(request.POST)

            if userTask.is_valid():
                dateAdd = userTask.cleaned_data["dateAdd"]
                timeAdd = userTask.cleaned_data["timeAdd"]
                taskAdd = userTask.cleaned_data["taskAdd"]

                # значения для добавления взятые выше
                value_for_update = {"title": taskAdd, "date": dateAdd, "time": timeAdd}

                # получаем ид пользователя
                current_user = request.user

                # добавление новой задачи даты ,времени и ид пользователя за которым закреплена задача
                newTask = Task.objects.update_or_create(defaults=value_for_update, id=None, user_id=current_user.id)

        return userTask
