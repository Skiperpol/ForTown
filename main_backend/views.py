from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateNewEvent
from .models import Event

def addEvent(response):
    if response.method == "POST":
        form = CreateNewEvent(response.POST)

        if form.is_valid():
            obj=Event()
            obj.title = form.cleaned_data["title"]
            obj.description = form.cleaned_data["description"]
            obj.author = response.user
            obj.start_time = form.cleaned_data["start_time"]
            obj.deadline = form.cleaned_data["deadline"]
            obj.type_of_event = form.cleaned_data["type_of_event"]
            obj.link_do_miejsca_wydarzenia = form.cleaned_data["link_do_miejsca_wydarzenia"]
            obj.x_miejsca = form.cleaned_data["x"]
            obj.y_miejsca = form.cleaned_data["y"]
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateNewEvent()
    return render(response, "frontend/home.html", {"form":form})
