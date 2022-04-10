from django.shortcuts import render, redirect
from main_backend.forms import CreateNewEvent
from main_backend.models import Event
# Create your views here.

def home_page(request):
    form = CreateNewEvent()
    event = Event.objects.all()
    context = {"form":form, "event":event}
    return render(request, 'home.html', context)