from django.shortcuts import render
from que_nome.models import Teams

# Create your views here.
def home(request):
    
    teams_list = Teams.objects.all()
    return render(request, 'pages/que_nome_home.html', {'teams_list':teams_list})
