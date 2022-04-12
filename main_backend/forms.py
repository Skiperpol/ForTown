from django import forms
from django.forms.widgets import NumberInput

TITLE_CHOICES = [
    ('Sportowe', 'Sportowe'),
    ('Kulturowe', 'Kulturowe'),
    ('Rozrywkowe', 'Rozrywkowe'),
]

# Tam gdzie masz task_window możesz dopisać sobie jak ma się nazywać klasa do danego okienka
class CreateNewEvent(forms.Form):
    title = forms.CharField(label='Nazwa wydarzenia', max_length=100, widget=forms.TextInput(attrs={'class':'task_window', 'placeholder':'Zawody sportowe'}))
    description = forms.CharField(label='Opis', max_length=300, widget=forms.Textarea(attrs={'class':'task_window', 'placeholder':'Otwarty turniej piłkarski'}))
    start_time = forms.DateField(label='Data rozpoczęcia', widget=NumberInput(attrs={'type': 'date', 'class':'task_date'}))
    deadline = forms.DateField(label='Przewidywana data zakończenia', widget=NumberInput(attrs={'type': 'date', 'class':'task_date'}))
    type_of_event = forms.CharField(label='Wybierz rodzaj wydarzenia',
        widget=forms.Select(choices = TITLE_CHOICES, attrs={'class':'task_window'}),
        required=True
    )
    link_do_miejsca_wydarzenia = forms.URLField(required=False, label='Link', max_length = 200, widget=forms.URLInput(attrs={'class':'task_window'}))
    x = forms.FloatField(label='Naciśnij na mapę aby wybrać współrzędne geograficzne', required=True, widget=forms.NumberInput(attrs={'id': 'x', 'step': "0.0000000001"}))
    y = forms.FloatField(label='', required=True, widget=forms.NumberInput(attrs={'id': 'y', 'step': "0.0000000001"}))

class TrwajaceForm(forms.Form):
    title =  forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'none', 'value':'trwa'}))
    
class KulturoweForm(forms.Form):
    title =  forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'none', 'value':'kulturowe'}))
    
class SportoweForm(forms.Form):
    title =  forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'none', 'value':'sportowe'}))
    
class RozrywkoweForm(forms.Form):
    title =  forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'none', 'value':'rozrywkowe'}))
    