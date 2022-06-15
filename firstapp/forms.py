from django import forms


class UserTask(forms.Form):
    dateAdd = forms.DateTimeField(label="Дата", help_text="Введите дату: Формат: день/месяц/год", widget=forms.DateInput(format='%d/%m/%Y'))
    timeAdd = forms.TimeField(label="Время", help_text="Выберите время: Формат: час:минуты")
    taskAdd = forms.CharField(label="Задача", help_text="Введите свою задачу", widget=forms.Textarea)
