import requests

# API key
api_key = 'ebb6d00fd74ac3c9629f4babca0acb68'
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Initialize an empty list to store weather data for each city
weather_data = []

for city in cities:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    print(data)

    # Extract relevant weather information
    temperature = data['main']['temp']
    temperature_min = data['main']['temp_min']
    temperature_max = data['main']['temp_max']
    feelsLike = data['main']['feels_like']
    humidity = data['main']['humidity']
    weather_condition = data['weather'][0]['description']

    # Create a dictionary for each city's weather data
    city_weather_data = {
        'city': city,
        'temperature': temperature,
        'temperature_min': temperature_min,
        'temperature_max': temperature_max,
        'feelsLike': feelsLike,
        'humidity': humidity,
        'weather_condition': weather_condition,
    }

    # Append the city's weather data to the list
    weather_data.append(city_weather_data)

# Print or use the weather data as needed
for data in weather_data:
    print(f"City: {data['city']}")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Temperature_MIN: {data['temperature_min']}°C")
    print(f"Temperature_MAX: {data['temperature_max']}°C")
    print(f"Feels Like: {data['feelsLike']}°C")
    print(f"Humidity: {data['humidity']}%")
    print(f"Weather Condition: {data['weather_condition']}")
    print("\n")

