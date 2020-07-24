from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from que_nome.models import Teams, Players
from home.blocks import CourseBlock, FreeCourseBlock, JobBlock, ProjectBlock

class ContactButton(models.Model):
    name = models.CharField(null=True, blank=False, max_length=20)
    link = models.URLField(null=True, blank=False)
    social_icon = models.CharField(null=True, blank=False, max_length=20)

    panels =[
        MultiFieldPanel(
        [
            FieldPanel('name', heading='Nome do Site'),
            FieldPanel('link', heading='Link'),
            FieldPanel('social_icon', heading='ID icone FontAwesome 5'),
        ],
        heading="Contato/Redes Social",
        classname="collapsible"
        )]

    def __str__(self):
        return self.name
register_snippet(ContactButton)

class TechIcon(models.Model):
    name = models.CharField(null=True, blank=False, max_length=20)
    tech_icon = models.CharField(null=True, blank=False, max_length=40)

    panels =[
        MultiFieldPanel(
        [
            FieldPanel('name', heading='Nome da Habilidade/Tecnologia'),
            FieldPanel('tech_icon', heading='ID icone FontAwesome 5'),
        ],
        heading="Habilidade/Tecnologia",
        classname="collapsible"
        )]

    def __str__(self):
        return self.name
register_snippet(TechIcon)

class ContactButtons(Orderable):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='contact_buttons')
    button = models.ForeignKey(ContactButton, on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel('button'),
    ]

class TechIcons(Orderable):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='tech_icons')
    tech_icon = models.ForeignKey(TechIcon, on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel('tech_icon'),
    ]

class Diferentials(Orderable):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='diferentials')
    text = models.CharField(null=True, blank=False, max_length=200)

    panels = [
        FieldPanel('text', heading='Meu Diferencial')
    ]

class HomePage(Page):
    # Campo Sobre Mim
    local = models.CharField(max_length=250)
    telefone = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    apresentacao = models.TextField(blank=True)
    citacao = models.CharField(max_length=250)

    # Campo Experiências
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

    # Campo Projetos
    projetos = StreamField(
        [
        ('projects', ProjectBlock())
        ],
        null=True,
        blank=True,
    )

    # Painéis da Página
    content_panels = Page.content_panels + [
        # Painéis Sobre Mim
        MultiFieldPanel(
        [
            FieldPanel('local', heading='Cidade, UF País'),
            FieldPanel('telefone', heading='Telefone com DDD'),
            FieldPanel('email', heading='Seu melhor E-mail'),
            FieldPanel('apresentacao', heading='Texto de Apresentação'),
            FieldPanel('citacao', heading='Relato de um Fã'),
            InlinePanel('contact_buttons', heading='Contatos/Redes Sociais', min_num=1),
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

        # Painéis Habilidades
        MultiFieldPanel(
        [
        MultiFieldPanel([InlinePanel('tech_icons', heading='Tecnologias', min_num=1, label="Técnologias",)],
        heading="Técnologias",
        classname="collapsible"),
        MultiFieldPanel([InlinePanel('diferentials', heading='Diferenciais', min_num=1, label="Diferenciais",)],
        heading="Diferenciais",
        classname="collapsible"),
        ],
        heading="Habilidades",
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

        # Painéis Experiências
        MultiFieldPanel(
        [
            StreamFieldPanel('projetos'),
        ],
        heading="Projetos",
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
