from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse
from urllib.parse import quote
from django.db.models import Count

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

from .models import Event, Case, Users
from .forms import add_event_form, link_event_form, add_case_form, CreateUserForm, LoginForm, DateRangeForm

import json, requests


# Create your views here.
def user_authentication(request):
    return HttpResponse("User authentication")


def register_page(request):
    
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = Users(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email_ad=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], chp_staff_no=form.cleaned_data['chp_staff_no'])
                new_user.save()
                return redirect('login')
                #return render(request, 'login.html')

        context = {'form':form}
        return render(request, 'register.html', context)


def login_page(request):

    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = LoginForm(request.POST)
        
        if request.method == 'POST':
            if form.is_valid():

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse("User authentication Failed")

        context = {'form':form}
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_page_view(request):
    case = Case.objects.all()
    context = {'object_list' : case}
    return render(request, 'home_page.html', context)


@login_required(login_url='login')
def ViewLocCase(request, case):
    events = Event.objects.filter(case=case)
    display_case = Case.objects.get(case_no=case)
    context = {'case_events_details' : events, 'case' : display_case} 
   
    return render(request, 'case_events_details.html', context)


@login_required(login_url='login')
def sse_display(request, event):

    #possible infected
    event_date = Event.objects.get(pk=event).event_date 
    start_infected, end_infected = event_date+timedelta(2), event_date+timedelta(14)
    infected = Case.objects.filter(event=event, symp_date__range=[start_infected, end_infected])

    #possible infector
    infector = Case.objects.filter(event=event, symp_date__lt = event_date+timedelta(3))

    context = {'infected' : infected, 'infector': infector, 'event' : Event.objects.get(pk=event)} 
    return render(request, 'sse_display.html', context)


@login_required(login_url='login')
def link_event_view(request, case):

    if request.method == 'POST':
        form = link_event_form(request.POST)

        if form.is_valid():
            case = Case.objects.get(pk=case)
            events = form.cleaned_data.get('events')
            case.event_set.add(*events)

            try:
                case.save()
                return HttpResponseRedirect(reverse('success'))
            except:
                return HttpResponseRedirect(reverse('error'))

        else:
            return HttpResponseRedirect(reverse('error'))
            
    else:
        form = link_event_form

    context = {'form': form}
    return render(request, 'link_case.html', context)


@login_required(login_url='login')
def add_case_view(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form object and populate it with data from the request (binding):
        form = add_case_form(request.POST)

        if form.is_valid():
            case_no = form.cleaned_data.get('case_no')
            name = form.cleaned_data.get('name')
            id_num = form.cleaned_data.get('id_num')
            dob = form.cleaned_data.get('dob')
            symp_date = form.cleaned_data.get('symp_date')
            confirm_date = form.cleaned_data.get('confirm_date')
            events = form.cleaned_data.get('events')
            
            
            for i in events:
                event_list = Event.objects.filter(name = i.name).values_list('event_date', flat=True)
                for i in event_list:
                    event_val = i
                dt_14_days_before_onset = symp_date - timedelta(14)
                if (event_val < dt_14_days_before_onset):
                    return HttpResponseRedirect(reverse('error'))

            new_case = Case(case_no=case_no, name=name, id_num=id_num,
            dob=dob, symp_date=symp_date, confirm_date=confirm_date)

            new_case.save()
            new_case.event_set.add(*events)
            new_case.save()
            
            try:
                new_case.save()
                return HttpResponseRedirect(reverse('success'))
            except:
                return HttpResponseRedirect(reverse('error'))

        else:
            return HttpResponseRedirect(reverse('error'))


    # If this is a GET (or any other method) then create the default form.
    else:
        form = add_case_form

    context = {'form': form}
    return render(request, 'add_case.html', context)


@login_required(login_url='login')
def add_event_view(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form object and populate it with data from the request (binding):
        form = add_event_form(request.POST)


        if form.is_valid():

            name = form.cleaned_data.get('name')
            location = form.cleaned_data.get('location')
            event_date = form.cleaned_data.get('event_date')
            description = form.cleaned_data.get('description')
            cases = form.cleaned_data.get('cases')
            
            for j in cases:
                symp_list = Case.objects.filter(case_no = j.case_no).values_list('symp_date', flat=True)
                for i in symp_list:
                    symp_val = i
                dt_14_days_before_onset = symp_val - timedelta(14)
                if (event_date < dt_14_days_before_onset):
                    return HttpResponseRedirect(reverse('error'))


            api_endpoint = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q='
            querystring = quote(location)
            response = requests.get(api_endpoint + querystring)

            # success retrieval
            if response.status_code == 200:

                # assumption: only 1 match
                address = response.json()[0]['addressEN']
                x_coor = response.json()[0]['x']
                y_coor = response.json()[0]['y']

                new_event = Event(name=name, location=location,
                address=address, x_coor=x_coor, y_coor=y_coor,
                event_date=event_date, description=description)

                new_event.save()
                new_event.case.add(*cases)
                new_event.save()

                try:
                    new_event.save()
                    return HttpResponseRedirect(reverse('success'))
                except:
                    return HttpResponseRedirect(reverse('error'))

            else:
                return HttpResponseRedirect(reverse('error'))

        else:
            return HttpResponseRedirect(reverse('error'))


    # If this is a GET (or any other method) then create the default form.
    else:
        form = add_event_form


    context = {'form': form}
    return render(request, 'add_event.html', context)


@login_required(login_url='login')
def SSE_date_range(request):
    if request.method == 'POST':

        # Create a form object and populate it with data from the request (binding):
        form = DateRangeForm(request.POST)

        if form.is_valid():
            from_date = form.cleaned_data.get('from_date')
            to_date = form.cleaned_data.get('to_date')

            temp_list = Event.objects.filter(event_date__range=[from_date, to_date])
            SSE_list = temp_list.annotate(num_case = Count('case')).filter(num_case__gte=6)


            #for i in SSE_list:

            context = {'form': form, 'case_events_details' : SSE_list}
            return render(request, 'date_range.html', context)

    else:
        form = DateRangeForm

    context = {'form': form}
    return render(request, 'date_range.html', context)


@login_required(login_url='login')
def success_view(request):
    return render(request, 'success.html')


@login_required(login_url='login')
def error_view(request):
    return render(request, 'error.html')
