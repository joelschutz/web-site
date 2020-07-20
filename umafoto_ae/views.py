from django.shortcuts import render

from umafoto_ae.photohunter import PhotoHunter


def home(request): 
    return render(request, 'pages/umafoto_ae_home.html')


def info(request): 
    return render(request, 'pages/umafoto_ae_info.html')


def fotos(request):
    return render(request, 'pages/umafoto_ae_result.html', PhotoHunter(request).get_photo())
