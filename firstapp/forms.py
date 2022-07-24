from django import forms
from TODO import settings


class UserTask(forms.Form):
    dateAdd = forms.DateField(label="Дата", help_text="Введите дату", input_formats=settings.DATE_INPUT_FORMATS)
    timeAdd = forms.TimeField(label="Время", help_text="Выберите время: Формат: час:минуты")
    taskAdd = forms.CharField(label="Задача", help_text="Введите свою задачу", widget=forms.Textarea)
