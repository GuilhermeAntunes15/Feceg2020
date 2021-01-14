from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def jogo_cores(request):
    return render(request, 'jogo_cores.html')

def tente_vc(request):
    return render(request, 'tente_vc.html')

def jogos(request):
    return render(request, 'jogos.html')

def videos(request):
    return render(request, 'videos.html')

def jogo_animals(request):
    return render(request, 'jogo_animals.html')

def tente_vc_animals(request):
    return render(request, 'tente_vc_animals.html')

def fale_conosco(request):
    return render(request, 'fale_conosco.html')

def corpoHumano(request):
    return render(request, 'corpoHumano.html')

def casa(request):
    return render(request, 'casa.html')