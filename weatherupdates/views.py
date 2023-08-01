
import requests

from datetime import datetime

from django.shortcuts import render, redirect
import json

from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
# def index(request):
#     try:
#         if request.method == 'POST':
#             API_KEY = '41dd2dad6c2d0f05c8927b84e1975b5a'
#             city_name = request.POST.get('city')
#             url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

#             response = requests.get(url).json()

#             current_time = datetime.now()

#             formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")

#             city_weather_update = {
#                 'city': city_name,
#                 'description': response['weather'][0]['description'],
#                 'icon': response['weather'][0]['icon'],
#                 'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
#                 'country_code': response['sys']['country'],
#                 'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
#                 'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
#                 'time': formatted_time
#             }

#         else:
#             city_weather_update = {}
        
#         context = {'city_weather_update': city_weather_update}
#         return render(request, 'weatherupdates/home.html', context)
    
#     except:
#         return render(request, 'weatherupdates/404.html')

# the index() will handle all the app's logic
def index(request):
    # if there are no errors the code inside try will execute
    try:
    # checking if the method is POST
        if request.method == 'POST':
            API_KEY = "4ec39eeea853eba976a2f2022ad32ebd"
            # getting the city name from the form input   
            city_name = request.POST.get('city')
            # the url for current weather, takes city_name and API_KEY   
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json   
            response = requests.get(url).json()
            # getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            # bundling the weather information in one dictionary

            city_weather_update = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
        # if the request method is GET empty the dictionary
        else:

            city_weather_update = {}

        context = {'city_weather_update': city_weather_update, 'city_name': city_name}
        return render(request, 'weatherupdates/home.html', context)
    
    # if there is an error the 404 page will be rendered 
    # the except will catch all the errors 
    except:
        return render(request, 'weatherupdates/404.html')
    

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("weather:home")