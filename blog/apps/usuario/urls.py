from django.urls import path
from django.contrib.auth import views as auth
from . import views

app_name="usuario"

urlpatterns = [
    path('usuario/', views.ListarPost, name="usuario"),
    path('login/',auth.LoginView.as_view(template_name="usuario/login.html"),name="login"),
    path('logout/',auth.LogoutView.as_view(),name="logout"),
    path('registrar/', views.RegistrarUsuario.as_view(), name="registrar")
]