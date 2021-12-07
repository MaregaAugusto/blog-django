from django.shortcuts import render

from .models import Post
# Create your views here.

def ListarPost(request, categoria):
    return render(request,'post/listapost.html',{"categoria":categoria})
	
    """ ser = Servicio.objects.get(id = id)
	dec = Denuncia.objects.filter(servicio = ser)
	if dec:
		messages.info(request, 'Usted ya realizo un reclamo de este servicio')
	else:
		if request.method == 'POST':
			asunto = request.POST.get('asunto')
			texto = request.POST.get('texto')
			den = Denuncia.objects.create(asunto = asunto, texto = texto, servicio = ser)
			den.save()
			messages.info(request, 'Su reclamo se ha registrado correctamente')
	return render(request,'servicios/denuncia.htm') """