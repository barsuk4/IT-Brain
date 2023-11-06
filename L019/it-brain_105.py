import requests
import os


def get_weather(api_key, city, country):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}'
    # url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        print('Помилка: Неможливо отримати погодні дані')
        return
    location = data['name']
    condition = data['weather'][0]['main']+ ", " + data['weather'][0]['description']
    temperature = data['main']['temp']-273.15
    print(f'Погода у місті {location}: {condition}')
    print(f'Температура: {temperature:.2f}°C')
# Ключ API та місто для тестування
api_key = os.getenv("WEATHER_API_KEY")
city = 'Kyiv'
get_weather(api_key, city, country='UA')
