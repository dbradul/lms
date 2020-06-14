from django.contrib import admin

# Register your models here.
from student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group')
    list_select_related = ('group',)
    list_per_page = 10
    search_fields = ('first_name',)


admin.site.register(Student, StudentAdmin)

class StudentAdminModel(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email')

