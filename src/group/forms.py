from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm

from group.models import Group

class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class GroupAddForm(GroupBaseForm):
    pass

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #
    #     already_exists = Group.objects.filter(
    #         Q(email=self.cleaned_data['email'])
    #     ).exists()
    #
    #     if already_exists:
    #         raise ValidationError(f"Student with email '{self.cleaned_data['email']}' already exists")
    #
    #     return email
    #
    # def clean_first_name(self):
    #     first_name = self.cleaned_data['first_name']
    #
    #     already_exists = Group.objects.filter(
    #         Q(first_name=self.cleaned_data['first_name'])
    #     ).exists()
    #
    #     if already_exists:
    #         raise ValidationError(f"Student with name '{self.cleaned_data['first_name']}' already exists")
    #
    #     return first_name


class GroupEditForm(GroupBaseForm):
    pass


