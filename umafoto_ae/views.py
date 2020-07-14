from django.shortcuts import render
from django.http import HttpResponse
from umafoto_ae.photohunter import ApiGetter


umafoto_ae = lambda request : render(request, 'pages/umafoto_ae_base.html')

def fotos(request):
    apigetter = ApiGetter()
    print('Pedindo Foto ao ApiGetter')
    tag = request.GET.get('tag', '')
    orientation = request.GET.get('orientation', '')
    color = request.GET.get('color', '')
    dic = apigetter.get_photo(tag, orientation, color)
    
    return render(request, 'pages/umafoto_ae_result.html', dic)
