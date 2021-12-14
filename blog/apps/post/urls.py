from django.urls import path, re_path
from . import views

app_name="post"

urlpatterns = [
    path('listarCategoria/<str:categoria>', views.ListarPostPorCategoria, name="listarCategoria"),
    re_path(r'^listarFecha/(?P<fecha>[0-9]{4}-?[0-9]{2}-?[0-9]{2})', views.ListarPostPorFecha, name="postFecha"),
    path('addcomentario/', views.AddComentario, name="addcomentario"),
    path('toppost/', views.GetTopPost, name='toppost'),
    path('readpost/<int:id>', views.ReadPost, name="readpost"),
    path('comentarios/', views.Comentarios, name="comentarios")
]
