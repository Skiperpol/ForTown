from django.shortcuts import render, redirect
from main_backend.forms import CreateNewEvent
from main_backend.models import Event
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def home_page(request):
    form = CreateNewEvent()
    event = Event.objects.all()
    context = {"form":form, "event":event}
    return render(request, 'home.html', context)
    
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect(frontend)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})
