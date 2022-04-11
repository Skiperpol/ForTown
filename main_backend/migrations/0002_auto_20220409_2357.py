# Generated by Django 3.2.11 on 2022-04-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='link_do_miejsca_wydarzenia',
            field=models.URLField(default=1213),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='x_miejsca',
            field=models.FloatField(default=23.3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='y_miejsca',
            field=models.FloatField(default='214'),
            preserve_default=False,
        ),
    ]