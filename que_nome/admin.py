
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Teams

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
