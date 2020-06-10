from django.db import models
from django.contrib import admin

# Create your models here.
from user_account.models import UserProfile

#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'group')
#     list_select_related = ('group',)
#     list_per_page = 10
#     search_fields = ('first_name',)


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'image') #, 'user__email')
    list_display = ('user', 'image') #, 'user__email')

    def user__email(self, instance):
        return instance.user.email

admin.site.register(UserProfile, UserProfileAdmin)
