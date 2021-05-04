from django import forms
from django.utils.safestring import mark_safe

from .models import *

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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

class link_event_form(forms.Form):
    events = forms.ModelMultipleChoiceField(queryset=Event.objects.all(), widget=forms.CheckboxSelectMultiple)


class LoginForm(forms.Form):
    username = forms.CharField(label = mark_safe('Username'))
    password = forms.CharField(label = mark_safe('Password'), widget=forms.PasswordInput)

class DateRangeForm(forms.Form):
    from_date = forms.CharField(label = mark_safe('From (yyyy-mm-dd)'))
    to_date = forms.CharField(label = mark_safe('To (yyyy-mm-dd)'))


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','chp_staff_no', 'email_ad' , 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','chp_staff_no', 'email_ad' , 'first_name', 'last_name')


