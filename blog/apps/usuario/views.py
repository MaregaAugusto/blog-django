from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegistroUsuarioFrom
# Create your views here.

def ListarPost(request):
    return render(request,'usuario/usuario.html')

class RegistrarUsuario(CreateView):
	model = User
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/registrar.html'
	success_url = reverse_lazy('usuario:login')
