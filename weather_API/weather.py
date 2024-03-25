#!/usr/bin/bash

import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        print(f"The current temperature in {city_name} is {temperature}°C.")

        if temperature <= 0:
            print("Seems it chilly ASF!! here , OMG!!!!")

        elif temperature > 0 and temperature <= 10:
            print("Mmmmh!, still cold though")

        elif temperature > 10 and temperature <= 30:
            print("not bad, habitable for me")

        else:
            print("goddamn hot , unless it's near beach , am not going, hell no!!")
    
    else:
        print("City not found. Please enter a valid city name.")

def main():
    api_key = "1412eef9bfe8682ee8e9f6e80f4f6ee8" # Replace "YOUR_API_KEY_HERE" with your actual API key
    city_name = input("Enter a city name: ").strip()
    get_weather(city_name, api_key)

if __name__ == "__main__":
    main()
