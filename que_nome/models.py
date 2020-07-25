from django.db import models
from wagtail.core.models import Page

class Teams(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=80)
    team_id = models.IntegerField(primary_key=True)
    team_url = models.URLField()
    team_logo = models.URLField()

    class Meta:
        ordering = ['team_id']

    def __str__(self):
        return self.name

class Players(models.Model):
    name = models.CharField(max_length=30)
    photo = models.URLField()

    birthday = models.DateField(blank=True, null=True)
    url = models.URLField()
    player_id = models.IntegerField(primary_key=True)
    teams = models.ManyToManyField(Teams)
    name_score = models.IntegerField()

    class Meta:
        ordering = ['player_id']

    def __str__(self):
        return self.name + ' Name Score: ' + str(self.name_score)

class TeamsPage(Page):
    template = 'que_nome/que_nome_home.html'
    def get_context(self, request, *args, **kwargs):
        """ Page for teams """
        context = super().get_context(request, *args, **kwargs)
        context['teams'] = Teams.objects.order_by('name')
        return context

class PlayersPage(Page):
    template = 'que_nome/que_nome_result.html'
    def get_context(self, request, *args, **kwargs):
        """ Page for players """
        context = super().get_context(request, *args, **kwargs)
        team = request.GET.get('team', '')

        if team:
            team_sel = Teams.objects.get(team_id=int(team))
            player_list = team_sel.players_set.all().order_by('name_score')

        context['team_sel'] = team_sel
        context['player_list'] = player_list
        return context
