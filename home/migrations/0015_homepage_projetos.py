# Generated by Django 3.0.3 on 2020-07-24 00:09

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_homepage_experiencias'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='projetos',
            field=wagtail.core.fields.StreamField([('projects', wagtail.core.blocks.StructBlock([('state', wagtail.core.blocks.ChoiceBlock(choices=[('developing', 'Em desenvolvimento'), ('done', 'Pronto'), ('deployed', 'Deployed')], help_text='Estado do desenvolvimento')), ('descrition', wagtail.core.blocks.CharBlock(help_text='Descrição do projeto', required=True)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Nome do Destino', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='URL do Destino', required=False))])))]))], blank=True, null=True),
        ),
    ]
