from django.urls import path

from applications.users import views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("home/", views.dashboard, name="dashboard"),
]
