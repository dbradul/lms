from django.urls import path
from student.views import (
    students_list,
    students_add,
    students_edit,
    students_delete
)

urlpatterns = [
    path('', students_list, name='students'),
    path('add/', students_add, name='student_add'),
    path('edit/<int:id>', students_edit, name='student_edit'),
    path('delete/<int:id>', students_delete, name='student_delete'),
]
