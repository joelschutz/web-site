# Generated by Django 3.0.3 on 2020-07-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200718_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='texto',
            field=models.TextField(blank=True),
        ),
    ]
