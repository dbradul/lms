"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from group.views import groups_list, group_edit
# from student.views import students_list, students_add, students_edit, students_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # path('groups/', groups_list, name='groups'),
    # path('groups/edit/<int:id>', group_edit, name='group_edit'),
    path('groups/', include('group.urls')),

    # path('students/', students_list, name='students'),
    # path('students/add/', students_add, name='student_add'),
    # path('students/edit/<int:id>', students_edit, name='student_edit'),
    # path('students/delete/<int:id>', students_delete, name='student_delete'),
    path('students/', include('student.urls')),

]
