from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateNewEvent
from .models import Event, Image
import datetime
from base64 import b64encode

def addEvent(response):
    if response.method == "POST":
        form = CreateNewEvent(response.POST, response.FILES)

        if form.is_valid():
            obj=Event()
            obj.title = form.cleaned_data["title"]
            obj.description = form.cleaned_data["description"]
            obj.main_image = response.FILES.get('main_image')
            obj.author = response.user
            obj.start_time = datetime.datetime.combine(form.cleaned_data["start_time"], form.cleaned_data["start_time_time"])
            obj.deadline = datetime.datetime.combine(form.cleaned_data["deadline"], form.cleaned_data["deadline_time"])
            obj.type_of_event = form.cleaned_data["type_of_event"]
            obj.link_do_miejsca_wydarzenia = form.cleaned_data["link_do_miejsca_wydarzenia"]
            obj.x_miejsca = form.cleaned_data["x"]
            obj.y_miejsca = form.cleaned_data["y"]
            obj.save()
            for images_loop in response.FILES.getlist('image'):
                image_obj = Image()
                image_obj.event = obj
                image_obj.image = images_loop
                image_obj.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateNewEvent()
    return render(response, "frontend/home.html", {"form":form})


