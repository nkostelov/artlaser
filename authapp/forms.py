import re
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'phone', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone':
                field.help_text = 'Формат номера +380881115522'
            else:
                field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Слишком молод еще!')
        return data

    def clean_phone(self):
        # Проверям номер телефона согласно стандарта E.164
        tmpl = re.compile(r'^\+{1}\d{10,14}\d$')
        data = self.cleaned_data['phone']
        result = re.match(tmpl, data)
        if not result:
            raise forms.ValidationError('Укажите номер в международном формате')
        else:
            return data


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'age', 'avatar', 'password')
        
    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone':
                field.help_text = 'Формат номера +380881115522'
            else:
                field.help_text = ''
            # Скрываем текущий пароль
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Слишком молод еще!')
        return data

    def clean_phone(self):
        # Проверям номер телефона согласно стандарта E.164
        tmpl = r'^\+{1}\d{10,14}\d$'
        data = self.cleaned_data['phone']
        result = re.match(tmpl, data)
        if not result:
            raise forms.ValidationError('Укажите номер в международном формате')
        else:
            return data
