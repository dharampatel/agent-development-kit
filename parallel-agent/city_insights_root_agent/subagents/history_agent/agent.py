from google.adk.agents import LlmAgent

from city_insights_root_agent.subagents.history_agent.tools import get_history_fact

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

history_agent = LlmAgent(
    name="HistoryAgent",
    model=GEMINI_MODEL,
    instruction="""You are a History Agent.

    Extract the city name from the user query and call the 'get_history_fact' tool.
    
    DO NOT make up historical info.
    
    Tool returns:
    - fact: a historical fact about the city
    
    Return something like:
    "Did you know that Paris was founded by the Parisii tribe in the 3rd century BC?"
    """,
    tools=[get_history_fact],
    output_key="history_fact"
)