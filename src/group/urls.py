from django.urls import path

from group.views import GroupsDeleteView, GroupsUpdateView, GroupsCreateView, GroupsListView

app_name = 'groups'

urlpatterns = [
    path('', GroupsListView.as_view(), name='list'),
    path('add', GroupsCreateView.as_view(), name='add'),
    path('edit/<int:pk>', GroupsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', GroupsDeleteView.as_view(), name='delete'),
]
