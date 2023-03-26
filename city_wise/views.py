from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.

def index(request):
    #return render(request,'index.html')
    # if there are no errors the code inside try will execute
    try:
#     # checking if the method is get 
        if 'city' in request.GET:
            API_KEY = 'd5c1828c47306b9cd6ea474da384c7d6'
            # getting the city name from the form input   
            city_name = request.GET.get('city')
            #city_name= 'banda'
            # the url for current weather, takes city_name and API_KEY   
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json   
            response = requests.get(url).json()
            #print(response)

#             # getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")          
#             # bundling the weather information in one dictionary
            city_weather_update = {
                'city': 'Today in '+ city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'F_temperature': str(response['main']['temp']*9/5+32)+'°F', 
                'temperature': 'Temperature: ' + str(response['main']['temp']) + '°C /',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
            context = {'city_weather_update':city_weather_update}
            # print(context)
            return render(request,'index.html',context)
        return render(request,'index.html')
    except:
         return render(request, '404.html')


# def error(request):
#      return render(request, '404.html')
  