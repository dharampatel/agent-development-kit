def get_fake_weather(city: str):
    """
        Returns fake weather information for a given city.
        """
    fake_weather = {
        "Paris": "Sunny, 24°C",
        "London": "Rainy, 18°C",
        "Tokyo": "Cloudy, 26°C"
    }
    return {"weather": fake_weather.get(city, "Weather data unavailable")}