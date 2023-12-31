from django.urls import path

from . import views


app_name = 'acccounts'

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("register/", views.register, name="user_registration")
]