# Generated by Django 3.1.5 on 2022-04-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_backend', '0007_auto_20220411_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Zaakceptowane', 'Zaakceptowane'), ('Odrzucone', 'Odrzucone')], default='Zaakceptowane', max_length=30),
            preserve_default=False,
        ),
    ]