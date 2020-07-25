
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Teams, Players

class TeamsAdmin(ModelAdmin):
    """Teams Admin"""
    model = Teams
    menu_label = 'Times'
    menu_icon = 'fa-futbol-o'
    menu_order = 300
    add_to_settings_menu = False
    excludde_from_explorer = False
    list_display = ('name', 'team_id',)
    search_fields = ('name', 'team_id')

modeladmin_register(TeamsAdmin)

class PlayersAdmin(ModelAdmin):
    """Players Admin"""
    model = Players
    menu_label = 'Jogadores'
    menu_icon = 'group'
    menu_order = 301
    add_to_settings_menu = False
    excludde_from_explorer = False
    list_display = ('name', 'player_id', 'name_score')
    search_fields = ('name', 'player_id')

modeladmin_register(PlayersAdmin)
