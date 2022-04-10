from pyexpat import model
from django.db import models
from django.forms import FloatField


TITLE_CHOICES = [
    ('Sportowe', 'Sportowe'),
    ('Kulturowe', 'Kulturowe'),
    ('Rozrywkowe', 'Rozrywkowe'),
]

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    start_time = models.DateField()
    deadline = models.DateField()
    type_of_event = models.CharField(max_length=30, choices=TITLE_CHOICES)
    link_do_miejsca_wydarzenia =  models.URLField(max_length = 200)
    x_miejsca = models.FloatField(null=True)
    y_miejsca = models.FloatField(null=True)

    def __str__(self):
        return self.title