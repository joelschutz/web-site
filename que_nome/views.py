from django.shortcuts import render
from que_nome.models import Teams, Players

# Create your views here.
def home(request):
<<<<<<< HEAD

    teams_list = Teams.objects.order_by('name')
    return render(request, 'que_nome/que_nome_home.html', {'teams_list':teams_list})
=======
    
    teams_list = Teams.objects.all().order_by('name')
    return render(request, 'pages/que_nome_home.html', {'teams_list':teams_list})
>>>>>>> 74158fa133f790eef2dbaacc7130963fa5c60e20

def team(request):
    team = request.GET.get('team', '')

    if team:
        team_sel = Teams.objects.get(team_id=int(team))
        player_list = team_sel.players_set.all().order_by('name_score')
<<<<<<< HEAD
        return render(request, 'que_nome/que_nome_result.html', {'players_list':player_list, 'team_sel':team_sel})
=======
        return render(request, 'pages/que_nome_result.html', {'players_list':player_list, 'team_sel':team_sel})

>>>>>>> 74158fa133f790eef2dbaacc7130963fa5c60e20
