from django.shortcuts import render, redirect
from main_backend.forms import CreateNewEvent, TrwajaceForm, KulturoweForm, SportoweForm, RozrywkoweForm, NadchodzaceForm
from main_backend.models import Event, Image
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
import datetime
from django.utils import timezone
# Create your views here.

def rodo(request):
    return render (request=request, template_name="rodo.html")

def polityka_prywatnosci(request):
    return render (request=request, template_name="polityka.html")

def trwajace(event, today, negative=False):
    event_query = event
    for e in event:
        trwa = (today + datetime.timedelta(hours=2)) >= (e.start_time + datetime.timedelta(hours=2))
        if not negative:
            if not trwa:
                event_query = event_query.exclude(id=e.id)
        else:
            if trwa:
                event_query = event_query.exclude(id=e.id)
    return event_query

def home_page(request):
    sort_key = 'all'
    form = CreateNewEvent()
    today = timezone.now()
    event = Event.objects.filter(status="Zaakceptowane").order_by("start_time")
    image = Image.objects.all()
    for e in event:
        if e.deadline < today:
                Event.objects.filter(id=e.id).delete()
                event = Event.objects.filter(status="Zaakceptowane").order_by("start_time")


    # tutaj sie dzieją sortowania, dziwnie to rozwiązałem, ale działa
    trwajace_form = TrwajaceForm(request.POST)
    kulturowe_form = KulturoweForm(request.POST)
    sportowe_form = SportoweForm(request.POST)
    rozrywkowe_form = RozrywkoweForm(request.POST)
    nadchodzace_form = NadchodzaceForm(request.POST)

    sortowane_eventy = event
    if request.method == "POST":
        if trwajace_form.is_valid():
            sort_key = trwajace_form.cleaned_data["title"]
            if sort_key == "trwa":
                trwajace_eventy = trwajace(event, today)
                sortowane_eventy = trwajace_eventy.order_by("deadline")
        if kulturowe_form.is_valid():
            sort_key = kulturowe_form.cleaned_data["title"]
            if sort_key == "kulturowe":
                sortowane_eventy = Event.objects.filter(type_of_event="Kulturowe", status="Zaakceptowane").order_by("start_time")
        if sportowe_form.is_valid():
            sort_key = sportowe_form.cleaned_data["title"]
            if sort_key == "sportowe":
                sortowane_eventy = Event.objects.filter(type_of_event="Sportowe", status="Zaakceptowane").order_by("start_time")
        if rozrywkowe_form.is_valid():
            sort_key = rozrywkowe_form.cleaned_data["title"]
            if sort_key == "rozrywkowe":
                sortowane_eventy = Event.objects.filter(type_of_event="Rozrywkowe", status="Zaakceptowane").order_by("start_time")
        if nadchodzace_form.is_valid():
            sort_key = nadchodzace_form.cleaned_data["title"]
            if sort_key == "incoming":
                trwajace_eventy = trwajace(event, today, True)
                sortowane_eventy = trwajace_eventy.order_by("deadline")

    trwajace_form = TrwajaceForm()
    kulturowe_form = KulturoweForm()
    sportowe_form = SportoweForm()
    rozrywkowe_form = RozrywkoweForm()
    nadchodzace_form = NadchodzaceForm()

    context = {"form":form, "trwajace_form":trwajace_form, 'kulturowe_form':kulturowe_form, 'sportowe_form':sportowe_form, 'rozrywkowe_form':rozrywkowe_form, 'nadchodzace_form':nadchodzace_form, "event":event,'today':today, 'sortowane_eventy':sortowane_eventy, 'sort_key':sort_key, 'image':image}
    return render(request, 'home.html', context)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect(home_page)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})
