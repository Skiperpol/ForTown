# Generated by Django 3.1.5 on 2022-04-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_backend', '0008_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Zaakceptowane', 'Zaakceptowane'), ('Odrzucone', 'Odrzucone'), ('Oczekuje', 'Oczekuje')], default='Oczekuje', max_length=30),
        ),
    ]
