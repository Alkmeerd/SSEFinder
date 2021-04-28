from django import forms
from django.utils.safestring import mark_safe

from .models import Case, Event

class add_case_form(forms.Form):
    case_no = forms.IntegerField(label = mark_safe('Case Number'))
    name = forms.CharField(label = mark_safe('Person Name'))
    id_num = forms.CharField(label = mark_safe('Identification Document Number'))
    dob = forms.DateField(label = mark_safe('Date of Birth (yyyy-mm-dd)'))
    symp_date = forms.DateField(label = mark_safe('Date of onset of symptoms (yyyy-mm-dd)'))
    confirm_date = forms.DateField(label = mark_safe('Date of confirmation by testing (yyyy-mm-dd)'))
    
    events = forms.ModelMultipleChoiceField(queryset=Event.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)


class add_event_form(forms.Form):
    name = forms.CharField(label = mark_safe('Venue Name'))
    location = forms.CharField(label = mark_safe('Venue Location'))
    event_date = forms.DateField(label = mark_safe('Date of event (yyyy-mm-dd)'))
    description = forms.CharField(label = mark_safe('Brief Description'), widget=forms.Textarea)

    cases = forms.ModelMultipleChoiceField(queryset=Case.objects.all(), widget=forms.CheckboxSelectMultiple)