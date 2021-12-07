from django.urls import path
from . import views

app_name="post"

urlpatterns = [
    path('listapost/<str:categoria>', views.ListarPost, name="listapost"),
]