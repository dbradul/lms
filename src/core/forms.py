from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm
from django import forms


# class RegisterUserForm(Form):
#     login = forms.CharField(max_length=64)
#     password = forms.PasswordInput()
#     email = forms.EmailField(max_length=64)

#
# class EmailValidator:
#     email_attribute_name = 'email'
#
#
#

class RegisterUserForm(UserCreationForm):
#     pass
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email')
#
# class RegisterUserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'password')

    # login = forms.CharField(max_length=64)
    # password = forms.PasswordInput()
    # email = forms.EmailField(max_length=64)
    class Meta(UserCreationForm.Meta):
        fields = ("username", 'email', 'first_name', 'last_name')
        # field_classes = {'username': UsernameField}

    def clean_email(self):
        email = self.cleaned_data['email']

        already_exists = User.objects. \
            filter(email=email). \
            exclude(id=self.instance.id). \
            count() > 0

        if already_exists:
            raise ValidationError('Email already exists!')

        return email


    def clean(self):

        return super().clean()

class ProfileUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # exclude = ('password', 'permissions', '_user_permissions', '_groups')
        fields = ("username", 'email', 'first_name', 'last_name')
    #     fields = ('first_name', 'last_name', 'username', 'email')

    # login = forms.CharField(max_length=64)
    # password = forms.PasswordInput()
    # email = forms.EmailField(max_length=64)

    def clean_email(self):
        email = self.cleaned_data['email']

        already_exists = User.objects. \
            filter(email=email). \
            exclude(id=self.instance.id). \
            count() > 0

        if already_exists:
            raise ValidationError('Email already exists!')

        return email