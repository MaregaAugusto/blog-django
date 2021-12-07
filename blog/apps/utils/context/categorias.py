from apps.utils.enum.categorias import categorias

def Categorias(request):
    return {'categorias' : categorias }
