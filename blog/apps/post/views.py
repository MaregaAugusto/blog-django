from django.shortcuts import render, redirect
from django.core.cache import cache
from django.views import View
from django.contrib.auth import views as auth


from .forms import ComentarioForm
from .models import Post, Comentario
# Create your views here.


def ListarPostPorCategoria(request, categoria):
	cache.clear()
	posts = Post.objects.filter(categoria=categoria)
	cache.set('posts', posts)
	context = { 
		'titulo': categoria,
		'posts': posts}
	return render(request,'post/base.html', context)

def ListarPostPorFecha(request, fecha):
	cache.clear()
	posts = Post.objects.filter(fecha=fecha)
	cache.set('posts', posts)
	context = {
		'titulo': fecha,
		'posts': posts
	}
	return render(request,'post/base.html', context)

def GetTopPost(request):
	cache.clear()
	posts = Post.objects.raw('SELECT pp.*, (SELECT count(*) FROM post_comentario as pc where pc.post_id = pp.id) as comentario FROM post_post as pp order by comentario desc limit 10')
	cache.set('posts', posts)
	context = {
		'titulo': 'top 10',
		'posts': posts
	}
	return render(request,'post/base.html', context)


""" class ReadPost(View):



	def get(self, request, id, *args, **kwargs):
		try:
			posts = ExistePost(id)
		except Exception:
			posts = Post.objects.get(id=id)
		comentarios = Comentario.objects.filter(post=id)
		form = ComentarioForm()
		context = {
			'titulo': 'post',
			'posts': posts,
			'form': form,
			'comentarios': comentarios
		}
		return render(request,'post/post.html', context)

	def post(self, request, id, *args, **kwargs):
		try:
			posts = ExistePost(id)
		except Exception:
			posts = Post.objects.get(id=id)
		comentarios = Comentario.objects.filter(post=id)

		form = ComentarioForm(request.POST)
		if form.is_valid():
			aux =  form.save(commit=False)
			aux.post = posts
			aux.save()
			form = ComentarioForm()

		context = {
			'titulo': 'post',
			'posts': posts,
			'form': form,
			'comentarios': comentarios
		}
		return render(request,'post/post.html', context)
 """
def ReadPost(request, id):
	try:
		posts = ExistePost(id)
	except Exception:
		posts = Post.objects.get(id=id)
	comentarios = Comentario.objects.filter(post=id)

	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated:
			aux =  form.save(commit=False)
			aux.post = posts
			aux.user = request.user
			aux.save()
			form = ComentarioForm()
		else:
			return redirect('usuario:login')
	
	context = {
		'titulo': 'post',
		'posts': posts,
		'form': form,
		'comentarios': comentarios
	}
	return render(request,'post/post.html', context)


def ExistePost(id):
	for i in cache.get('posts'):
		if i.id == id:
			return i
	return None

########################################################################
#                       views Comentario                               #
########################################################################


def AddComentario(request):
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)

def Comentarios(request):
	return render(request,'comentario/listarcomentario.html')