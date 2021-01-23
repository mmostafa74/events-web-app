from django import forms

from applications.events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "date"]


class SearchForm(forms.Form):
    query = forms.CharField()
