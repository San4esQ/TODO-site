from django import forms


class UserTask(forms.Form):
    dateAdd = forms.DateField(label="Дата", help_text="Введите дату: Формат: год-месяц-день")
    timeAdd = forms.TimeField(label="Время", help_text="Выберите время: Формат: час:минуты")
    taskAdd = forms.CharField(label="Задача", help_text="Введите свою задачу", widget=forms.Textarea)


class UserLogin(forms.Form):
    usernameAdd = forms.CharField(label="Логин", help_text="Введите логин", min_length=3)
    passwordAdd = forms.CharField(label="Пароль", help_text="Придумайте пароль", min_length=8,
                                  widget=forms.PasswordInput())
