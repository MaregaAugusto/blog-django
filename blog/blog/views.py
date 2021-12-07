from django.shortcuts import render
from apps.utils.enum.categorias import categorias

def Index(request):
    
    return render(request, 'Index.html')

