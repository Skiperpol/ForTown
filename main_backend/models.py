from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.forms import FloatField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

TITLE_CHOICES = [
    ('Sportowe', 'Sportowe'),
    ('Kulturowe', 'Kulturowe'),
    ('Rozrywkowe', 'Rozrywkowe'),
]

STATUS_AKCEPTACJI = [
    ('Zaakceptowane', 'Zaakceptowane'),
    ('Odrzucone', 'Odrzucone'),
    ('Oczekuje', 'Oczekuje'),
]

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    main_image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.CharField(max_length=50, null=True, blank=True)
    start_time = models.DateTimeField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=30, choices=STATUS_AKCEPTACJI, default="Oczekuje")
    type_of_event = models.CharField(max_length=30, choices=TITLE_CHOICES)
    link_do_miejsca_wydarzenia =  models.URLField(max_length = 200, blank=True, null=True)
    x_miejsca = models.FloatField(null=True)
    y_miejsca = models.FloatField(null=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    event = models.ForeignKey(Event, default=None, related_name='events', on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self):
        return self.event.title


# def dodaj_autora(sender, instance, created, **kwargs):
#     event = Event.objects.filter(id=instance.id).update(author=User.objects.get(username=request.user.username))

# # post_save.connect(dodaj_autora, sender=Event)
