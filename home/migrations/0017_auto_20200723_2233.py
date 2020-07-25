# Generated by Django 3.0.3 on 2020-07-24 01:33

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20200723_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('link', models.URLField(null=True)),
                ('social_icon', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('tech_icon', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='homepage',
            name='projetos',
            field=wagtail.core.fields.StreamField([('projects', wagtail.core.blocks.StructBlock([('state', wagtail.core.blocks.ChoiceBlock(choices=[('developing', 'Em desenvolvimento'), ('done', 'Pronto'), ('deployed', 'Deployed'), ('terminated', 'Fora do Ar')], help_text='Estado do desenvolvimento')), ('descrition', wagtail.core.blocks.CharBlock(help_text='Descrição do projeto', required=True)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Nome do Destino', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='URL do Destino', required=False))], icon='link')))]))], blank=True, null=True),
        ),
    ]