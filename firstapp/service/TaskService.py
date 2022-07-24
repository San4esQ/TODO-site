from firstapp.models import Task


class Index:
    def index(self, request):
        current_user = request.user
        tasks = Task.objects.filter(user=current_user)

        result = {}

        for task in tasks:
            key = task.date

            result.setdefault(key, []).append(task)

        return result


