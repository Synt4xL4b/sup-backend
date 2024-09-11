from django.urls import path

from views.users.login import UserLogin
from views.users.password import ChangePasswordView
from views.users.registry import SignUpView
from views.users.user_list import UserListView

app_name = "apps.users"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", UserLogin.as_view(), name="login"),
    path("password/", ChangePasswordView.as_view(), name="password"),
    path("list/", UserListView.as_view(), name="user_list"),
]
