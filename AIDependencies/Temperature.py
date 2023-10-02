from API_KEYS_FOR_FRIENDS import Weather_URL
import requests
import datetime


Weather_URL=Weather_URL


def TemperatureFormat():
    request_weather=requests.get(Weather_URL).json()

    #Takes the currenct date
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")

    #takes the actual hour and puts it in the format needed for the weatherapi
    formatted_datetime = formatted_datetime.split(" ")
    formatted_datetime.insert(1,"T")
    formatted_datetime="".join(formatted_datetime)
    return f"{formatted_datetime[0:13]}:00", request_weather