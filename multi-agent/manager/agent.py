from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst
from .tools.tools import get_current_time

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""   
    You are a manager agent that oversees other agents and delegates tasks accordingly.
    
    - For stock-related queries, delegate to the `stock_analyst`.
    - For nerdy jokes, delegate to the `funny_nerd`.
    - For news questions, use the `news_analyst` tool.
    
    Use context from recent interactions to make decisions. Allow users to switch topics freely (e.g., from news to jokes).
    
    Only respond directly if no sub-agent or tool matches the request.
    """,
    sub_agents=[stock_analyst, funny_nerd],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)