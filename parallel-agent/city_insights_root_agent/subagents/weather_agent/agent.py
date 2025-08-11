from google.adk.agents import LlmAgent

from city_insights_root_agent.subagents.weather_agent.tools import get_fake_weather

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

weather_agent = LlmAgent(
    name="weather_agent",
    model=GEMINI_MODEL,
    instruction="""You are a Weather Agent.

    Extract the city name from the user query and call the 'get_fake_weather' tool.
    
    DO NOT generate weather data yourself.
    
    Tool returns:
    - weather: fake weather info for the city
    
    Return just a sentence like:
    "The weather in Paris is sunny and 24°C."
    """,
    tools=[get_fake_weather],
    output_key="weather_info"
)