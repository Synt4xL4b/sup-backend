from django.urls import path

from controllers.users.login import UserLogin
from controllers.users.registry import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", UserLogin.as_view(), name="login"),
]
