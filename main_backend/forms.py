from django import forms
from django.forms.widgets import NumberInput

TITLE_CHOICES = [
    ('Sportowe', 'Sportowe'),
    ('Kulturowe', 'Kulturowe'),
    ('Rozrywkowe', 'Rozrywkowe'),
]

# Tam gdzie masz task_window możesz dopisać sobie jak ma się nazywać klasa do danego okienka
class CreateNewEvent(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'task_window'}))
    description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class':'task_window'}))
    author = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'task_window'}))
    start_time = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'class':'task_date'}))
    deadline = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'class':'task_date'}))
    type_of_event = forms.CharField(
        widget=forms.Select(choices = TITLE_CHOICES, attrs={'class':'task_window'}),
        required=True
    )
    link_do_miejsca_wydarzenia = forms.URLField(max_length = 200, widget=forms.URLInput(attrs={'class':'task_window'}))