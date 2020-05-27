from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form, ModelForm
from django import forms


# class RegisterUserForm(Form):
#     login = forms.CharField(max_length=64)
#     password = forms.PasswordInput()
#     email = forms.EmailField(max_length=64)


# class RegisterUserForm(UserCreationForm):
#     pass
    # class Meta:
    #     model = User
    #     fields = ('first_name', 'last_name', 'username', 'email')
#
class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
    # login = forms.CharField(max_length=64)
    # password = forms.PasswordInput()
    # email = forms.EmailField(max_length=64)
