from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from que_nome.models import Teams, Players
from home.blocks import CourseBlock, FreeCourseBlock, JobBlock


class HomePage(Page):
    # Campo Sobre Mim
    apresentacao = models.TextField(blank=True)
    citacao = models.CharField(max_length=250)

    # Campo Experiênce
    experiencias = StreamField(
        [
        ('jobs', JobBlock())
        ],
        null=True,
        blank=True,
    )

    # Campo Formações
    formacoes = StreamField(
        [
        ('formal_courses', CourseBlock()),
        ('free_courses', FreeCourseBlock())
        ],
        null=True,
        blank=True,
    )

    # Campo Interesses
    interesses = RichTextField(blank=True)

    # Painéis da Página
    content_panels = Page.content_panels + [
        # Painéis Sobre Mim
        MultiFieldPanel(
        [
            FieldPanel('apresentacao', classname="full", heading='Texto de Apresentação'),
            FieldPanel('citacao', heading='Relato de um Fã'),
        ],
        heading="Sobre Mim",
        classname="collapsible collapsed"
        ),

        # Painéis Experiências
        MultiFieldPanel(
        [
            StreamFieldPanel('experiencias'),
        ],
        heading="Experiência",
        classname="collapsible collapsed"
        ),

        # Painéis Formações
        MultiFieldPanel(
        [
            StreamFieldPanel('formacoes'),
        ],
        heading="Formação",
        classname="collapsible collapsed"
        ),

        # Painéis Interesses
        MultiFieldPanel(
        [
            FieldPanel('interesses'),
        ],
        heading="Interesses",
        classname="collapsible collapsed"
        ),
    ]

class HomePageQueNome(Page):
    template = 'que_nome/que_nome_home.html'
    def get_context(self, request, *args, **kwargs):
        """ Teams for page """
        context = super().get_context(request, *args, **kwargs)
        context['teams'] = Teams.objects.order_by('name')
        return context
