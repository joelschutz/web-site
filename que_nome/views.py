from django.shortcuts import render
from que_nome.models import Teams, Players

# Create your views here.
def home(request):
    
    teams_list = Teams.objects.all().order_by('name')
    return render(request, 'pages/que_nome_home.html', {'teams_list':teams_list})

def team(request):
    team = request.GET.get('team', '')

    if team:
        team_sel = Teams.objects.get(team_id=int(team))
        player_list = team_sel.players_set.all().order_by('name_score')
        return render(request, 'pages/que_nome_result.html', {'players_list':player_list, 'team_sel':team_sel})

