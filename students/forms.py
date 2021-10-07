from django.forms import ModelForm
from django.core.validators import ValidationError
from students.models import Student


class StudentCreateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']

        if 'elon' in email.lower():
            raise ValidationError('No more Elons, please!')

        return email

    def clean(self):
        pass