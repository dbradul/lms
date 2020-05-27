from django.urls import path

from user_account.views import CreateUserAccountView

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
]
