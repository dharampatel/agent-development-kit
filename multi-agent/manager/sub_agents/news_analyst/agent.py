from google.adk.agents import Agent
from google.adk.tools import google_search

news_analyst = Agent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="News analyst agent",
    instruction="""   
    You are a helpful news analyst agent.

    When the user asks for news:
    1. Use the google_search tool to search for news based on their query.
    2. If they refer to a relative time (e.g., "today", "this week"), use get_current_time to build the query.
    3. Provide a brief summary of relevant news items.
    
    If the request is not clearly a news question:
    - Do NOT reply or guess.
    - Return control to the manager to decide.
    """,
    tools=[google_search],
)