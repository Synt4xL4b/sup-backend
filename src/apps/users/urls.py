from django.urls import path

from views.users.login import UserLogin
from views.users.password import ChangePasswordView
from views.users.registry import SignUpView

app_name = "app.users"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", UserLogin.as_view(), name="login"),
    path("password/", ChangePasswordView.as_view(), name="password"),
]
