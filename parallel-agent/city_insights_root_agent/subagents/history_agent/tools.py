def get_history_fact(city: str):
    """
    :param city:
    :return: history about the cities
    """
    facts = {
        "Paris": "Paris was founded in the 3rd century BC by a Celtic tribe called the Parisii.",
        "London": "The Great Fire of London in 1666 destroyed most of the medieval city.",
        "Tokyo": "Tokyo was originally a small fishing village called Edo."
    }
    return {"fact": facts.get(city, "No historical fact available.")}