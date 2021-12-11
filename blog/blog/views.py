from django.shortcuts import render, redirect


def Index(request):
    try:
        if request.GET['fecha'] is not None:
            print('estoy en el index')
            return redirect('post/listarFecha/'+request.GET['fecha'])
    except :
        return render(request, 'Index.html')

def Index2(request):
 
    return render(request, 'indexb.html')