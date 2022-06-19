from django import forms


class UserTask(forms.Form):
    dateAdd = forms.DateTimeField(label="Дата", help_text="Введите дату: Формат: год-месяц-день")
    timeAdd = forms.TimeField(label="Время", help_text="Выберите время: Формат: час:минуты")
    taskAdd = forms.CharField(label="Задача", help_text="Введите свою задачу", widget=forms.Textarea)
