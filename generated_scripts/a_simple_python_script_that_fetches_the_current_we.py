import requests

def get_weather(api_key, city):
    """
    Fetches the current weather for a given city using the OpenWeatherMap API.

    Parameters:
    - api_key: str, your OpenWeatherMap API key
    - city: str, the city for which to fetch the weather

    Returns:
    - dict: weather data if successful, None otherwise
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    return None

def print_weather(weather_data):
    """
    Prints the weather data in a user-friendly format.

    Parameters:
    - weather_data: dict, the weather data to print
    """
    if weather_data:
        city = weather_data.get('name')
        temp = weather_data['main'].get('temp')
        description = weather_data['weather'][0].get('description')
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print("Could not retrieve weather data.")

def main():
    """
    Main function to execute the weather fetching and printing.
    """
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)
    print_weather(weather_data)

if __name__ == "__main__":
    main()