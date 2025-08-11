from google.adk.agents import LlmAgent

from city_insights_root_agent.subagents.travel_tip_agent.tools import get_travel_tip

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

travel_tip_agent = LlmAgent(
    name="travel_tip_agent",
    model=GEMINI_MODEL,
    instruction="""You are a Travel Tip Agent.

    Your task is to extract the city name from the query and call 'get_travel_tip'.
    
    DO NOT generate travel tips yourself.
    
    Tool returns:
    - tip: a useful travel tip for the city
    
    Return something like:
    "When in Tokyo, get a Suica card for easy metro travel."
    """,
    tools=[get_travel_tip],
    output_key="travel_tip"
)