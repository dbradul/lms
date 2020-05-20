from django.urls import path
from group.views import (
    group_list,
    group_add,
    group_edit,
    group_delete
)

urlpatterns = [
    path('', group_list, name='groups'),
    path('add/', group_add, name='group_add'),
    path('edit/<int:id>', group_edit, name='group_edit'),
    path('delete/<int:id>', group_delete, name='group_delete'),
]
