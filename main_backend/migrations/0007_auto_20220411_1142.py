# Generated by Django 3.1.5 on 2022-04-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_backend', '0006_auto_20220411_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
