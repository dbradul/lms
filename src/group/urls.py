from django.urls import path

from group.views import groups_list, group_edit

app_name = 'group'

urlpatterns = [
    path('', groups_list, name='list'),
    path('edit/<int:id>', group_edit, name='edit'),
]
