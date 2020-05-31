from django.contrib import admin

# Register your models here.
from student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group')
    list_select_related = ('group',)
    # list_filter = ('first_name', 'email')
    list_per_page = 10
    # list_max_show_all = 200
    # list_editable = ()
    search_fields = ('first_name',)
    # date_hierarchy = None
    # save_as = False
    # save_as_continue = True
    # save_on_top = False
    # paginator = Paginator
    # preserve_filters = True
    # inlines = []


admin.site.register(Student, StudentAdmin)