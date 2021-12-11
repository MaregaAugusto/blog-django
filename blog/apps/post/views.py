from django.shortcuts import render

from .forms import ComentarioForm
from .models import Post
# Create your views here.


def ListarPostPorCategoria(request, categoria):
	posts = Post.objects.filter(categoria=categoria)
	context = { 
		'titulo': categoria,
		'posts': posts}
	return render(request,'post/base.html', context)

def ListarPostPorFecha(request, fecha):
	posts = Post.objects.filter(fecha=fecha)
	context = {
		'titulo': fecha,
		'posts': posts
	}
	return render(request,'post/base.html', context)

def AddComentario(request):
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)