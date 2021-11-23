from django.urls import path
from . import views

app_name = "login"   

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("entrar", views.login_request, name="entrar"),
    path("logout", views.logout_request, name= "logout"),
]