import csv
from io import StringIO
from django.shortcuts import render
from django.views.generic import TemplateView
import json
import urllib.request

def home(request):
    return render(request, 'home.html', {})

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        encoded_city = urllib.parse.quote(city)
        api_key = ''
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{encoded_city}?unitGroup=us&include=days&key={api_key}&contentType=csv'
        
        source = urllib.request.urlopen(url).read()
        source = source.decode('utf-8') 
        
        csv_data = StringIO(source) 
        csv_reader = csv.DictReader(csv_data)
        
        data = {'csv_data': csv_reader}
    else:
        data = {}
    return render(request, "weather.html", data)