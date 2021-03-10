from django.shortcuts import render
from . import models
import requests

# Create your views here.

def home(request):

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=847ad8d22725feb921178a969b049211'
	if request.method=='POST':
		city=request.POST['city']
		
		

		r = requests.get(url.format(city)).json()
		# print(r)
		weather = {
			'city': city,
			'temperature': r["main"]["temp"],
			'humidity': r["main"]["humidity"],
			'description': r["weather"][0]["description"],
			'icon': r["weather"][0]["icon"],
		}
		data= models.weather(city=city, desc=r["weather"][0]["description"], temp=r["main"]["temp"],humidity=r["main"]["humidity"])
		data.save()
		# print(weather)
		context = {'location_weather' : weather}
		
		return render(request, 'index.html',context)
	else:

		city = 'kolkata'

		r = requests.get(url.format(city)).json()
		# print(r)
		weather = {
			'city': city,
			'temperature': r["main"]["temp"],
			'humidity': r["main"]["humidity"],
			'description': r["weather"][0]["description"],
			'icon': r["weather"][0]["icon"],
		}
		# print(weather)
		context = {'location_weather' : weather}
		
		return render(request, 'index.html',context)
	return render(request, 'index.html')