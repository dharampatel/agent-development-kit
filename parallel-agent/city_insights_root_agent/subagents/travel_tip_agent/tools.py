def get_travel_tip(city: str):
    """
        Returns travel tip about the cities
        """
    tips = {
        "Paris": "Buy tickets for the Eiffel Tower online to skip queues.",
        "London": "Use an Oyster card to travel easily around the city.",
        "Tokyo": "Get a Suica card and explore Tokyo by train."
    }
    return {"tip": tips.get(city, "No travel tip available.")}
