# Generated by Django 3.0.3 on 2020-07-24 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0021_auto_20200724_0034'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomePageQueNome',
        ),
    ]
