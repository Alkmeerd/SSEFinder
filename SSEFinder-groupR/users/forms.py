from django import forms
from django.utils.safestring import mark_safe


class add_case_form(forms.Form):
    case_no = forms.IntegerField(label = mark_safe('Case Number'))
    name = forms.CharField(label = mark_safe('</br>Person Name'))
    id_num = forms.CharField(label = mark_safe('<br>Identification Document Number'))
    dob = forms.DateField(label = mark_safe('<br>Date of Birth (yyyy-mm-dd)'))
    symp_date = forms.DateField(label = mark_safe('<br>Date of onset of symptoms (yyyy-mm-dd)'))
    confirm_date = forms.DateField(label = mark_safe('<br>Date of confirmation by testing (yyyy-mm-dd)'))


class add_event_form(forms.Form):
    name = forms.CharField(label = mark_safe('Venue Name'))
    location = forms.CharField(label = mark_safe('</br>Venue Location'))
    event_date = forms.DateField(label = mark_safe('<br>Date of event (yyyy-mm-dd)'))
    description = forms.CharField(label = mark_safe('<br><br>Brief Description</br>'), widget=forms.Textarea)
