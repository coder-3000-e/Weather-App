import csv
from io import StringIO
from django.shortcuts import render
from django.views.generic import TemplateView
import urllib.request
from weatherApp_project import settings

from weatherApp_project.settings import VISUALCROSSING_API_KEY

def home(request):
    return render(request, 'home.html', {})

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        encoded_city = urllib.parse.quote(city)
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{encoded_city}?unitGroup=uk&include=days&key={VISUALCROSSING_API_KEY}&contentType=csv'
        
        source = urllib.request.urlopen(url).read()
        source = source.decode('utf-8') 
        
        csv_data = StringIO(source) 
        csv_reader = csv.DictReader(csv_data)
        
        data = {'csv_data': csv_reader, 'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY}
    else:
        data = {'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY}
    return render(request, "weather.html", data)