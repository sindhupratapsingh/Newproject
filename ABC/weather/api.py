
import requests

def get_weather_data(city):
    api_key = 'https://www.worldweatheronline.com/widget/v5/weather-widget.ashx?loc=1122691&wid=4&tu=1&div=wwo-weather-widget-4'
    base_url = 'https://www.worldweatheronline.com/widget/v5/weather-widget.ashx?loc=1122691&wid=4&tu=1&div=wwo-weather-widget-4'
    params = {'key': api_key, 'q': city}
    
    response = requests.get(base_url, params=params)
    data = response.json()
    return data
