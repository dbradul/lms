import django_filters
from django import forms

from django_filters import FilterSet
from student.models import Student


class StudentListFilter(FilterSet):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

    first_name = django_filters.CharFilter(
        field_name='first_name',
        lookup_expr='icontains',
        # widget=forms.CharField(
        #     # widget={
        #     #     'class': 'form-control',
        #     #     'type': 'text',
        #     # }
        # ))
    )