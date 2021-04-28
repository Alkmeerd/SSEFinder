from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse
from urllib.parse import quote

from .models import Event, Case
from .forms import add_event_form, add_case_form

import json, requests


# Create your views here.
def user_authentication(request):
    return HttpResponse("User authentication")

class home_page_view(ListView):
    model = Case
    template_name = 'home_page.html'


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

            new_case = Case(case_no=case_no, name=name, id_num=id_num,
            dob=dob, symp_date=symp_date, confirm_date=confirm_date)

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

            api_endpoint = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q='
            querystring = quote(f'{name} {location}')
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
                print([i for i in range(100)])

                new_event.save()
                #return HttpResponseRedirect(reverse('find'))

                #return HttpResponseRedirect(reverse('error'))

            #else:
                #return HttpResponseRedirect(reverse('error'))

        #else:
            #return HttpResponseRedirect(reverse('error'))


    # If this is a GET (or any other method) then create the default form.
    else:
        form = add_event_form


    context = {'form': form}
    return render(request, 'add_event.html', context)


class success_view(TemplateView):
    template_name = 'success.html'

class error_view(TemplateView):
    template_name = 'error.html'

class view_case_details(TemplateView):
    template_name = 'locvisitedcase.html'

    def get_context_data(self, **kwargs):

        case = self.kwargs['case']

        context = super().get_context_data(**kwargs)
        context['events_list'] = Event.objects.filter(case__pk = case)
        context['case'] = Case.objects.get(pk = case)
        
        return context
    