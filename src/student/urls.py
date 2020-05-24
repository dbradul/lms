from django.contrib import admin
from django.urls import path

from group.views import groups_list, group_edit
# from student.views import students_list, students_add, students_edit, students_delete, StudentListView, \
from student.views import (
    StudentListView,
    StudentUpdateView,
    StudentCreateView,
    StudentDeleteView
)

app_name = 'student'

urlpatterns = [
    # path('', students_list, name='list'),
    path('', StudentListView.as_view(), name='list'),
    # path('add/', students_add, name='add'),
    path('add/', StudentCreateView.as_view(), name='add'),
    # path('edit/<int:id>', students_edit, name='edit'),
    path('edit/<int:pk>', StudentUpdateView.as_view(), name='edit'),
    # path('delete/<int:id>', students_delete, name='delete'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='delete'),
]
