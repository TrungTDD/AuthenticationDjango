from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>", views.detail_user, name="detail"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout")

]
