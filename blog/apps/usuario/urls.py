from django.urls import path
from . import views

app_name="usuario"

urlpatterns = [
    path('usuario/', views.ListarPost, name="usuario"),
]