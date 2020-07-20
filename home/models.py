from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from que_nome.models import Teams, Players


class HomePage(Page):
    # Campo Sobre Mim
    apresentacao = RichTextField(blank=True)
    citacao = models.CharField(max_length=250)

    # Campo Experiência
    texto = models.TextField(blank=True)

    # Painéis da Página
    content_panels = Page.content_panels + [
        # Painéis Sobre Mim
        FieldPanel('apresentacao', classname="full", heading='Texto de Apresentação'),
        FieldPanel('citacao', heading='Relato de um Fã'),

        # Painéis Experiência
        FieldPanel('texto'),
    ]

class HomePageQueNome(Page):
    template = 'que_nome/que_nome_home.html'
    def get_context(self, request, *args, **kwargs):
        """ Teams for page """
        context = super().get_context(request, *args, **kwargs)
        context['teams'] = Teams.objects.order_by('name')
        return context
