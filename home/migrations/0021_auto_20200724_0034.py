# Generated by Django 3.0.3 on 2020-07-24 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200724_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diferentials',
            name='text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]