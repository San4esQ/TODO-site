from firstapp.models import Task


class Edit:
    def edit(self, request, num):
        task = Task.objects.get(id=num)

        if request.method == "POST":
            task.date = request.POST.get("date")
            task.time = request.POST.get("time")
            task.title = request.POST.get("title")
            task.save()

        return task
