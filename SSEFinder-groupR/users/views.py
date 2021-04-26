from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import quote
import json, requests

# Create your views here.
 
def user_authentication(request):
    return HttpResponse("User authentication")
 
 
# Geodata Store API
venue_name = 'Kam Lok Hin Chicken and Fish Pot'
venue_location = 'Conwell Mansion'
api_endpoint = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q='
querystring = quote(f'{venue_name} {venue_location}')
#print(api_endpoint + querystring)
response = requests.get(api_endpoint + querystring)
#print(response)

if response.status_code == 200:
    # assumption: only 1 match
    address = response.json()[0]['addressEN']
    X_Coord = response.json()[0]['x']
    Y_Coord = response.json()[0]['y']

    #print(address)
    #print(X_Coord)
    #print(Y_Coord)
 
