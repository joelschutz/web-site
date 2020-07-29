import csv, datetime
from .models import Teams, Players

def import_teams(file):
    with open(file, 'rt') as f:
        reader = csv.DictReader(f)

        for team in reader:
            t = Teams(
            name = team['team_name'],
            full_name = team['team_full_name'],
            team_id = team['team_id'],
            team_url = 'https://www.transfermarkt.com' + team['team_name'],
            team_logo = team['team_logo']
            )
            t.save()
            print(f'Time salvo: {t.name}')

def import_players(file):
    with open(file, 'rt') as f:
        reader = csv.DictReader(f)

        for player in reader:

            p = Players(
            name = player['name'],
            photo = player['photo'],
            birthday = datetime.datetime.strptime(
            ('01/01/1900' if player['birthday'] == 'S/D' else player['birthday']),
             '%d/%m/%Y'),
            url = 'https://www.transfermarkt.com' + player['url'],
            player_id = player['player_id'],
            name_score = player['name_score']
            )
            p.save()
            teams = player['teams'].strip(' []')
            teams = teams.split(',')
            for team in teams:
                p.teams.add(Teams.objects.get(team_id=int(team)))
                p.save()
            print(f'Jogador Salvo salvo: {p}')
