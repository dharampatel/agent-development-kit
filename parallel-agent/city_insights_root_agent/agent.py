from google.adk.agents import ParallelAgent, SequentialAgent

from city_insights_root_agent.subagents.weather_agent.agent import weather_agent
from city_insights_root_agent.subagents.history_agent.agent import history_agent
from city_insights_root_agent.subagents.travel_tip_agent.agent import travel_tip_agent
from city_insights_root_agent.subagents.summary_agent.agent import summary_agent

# --- 1. Create Parallel Agent to gather information concurrently ---
parallel_insight_agent = ParallelAgent(
    name="city_info_gatherer",
    description="Gathers insights about a city using 3 specialized agents in parallel.",
    sub_agents=[
        weather_agent,
        travel_tip_agent,
        history_agent
    ],
)

# --- 2. Create Sequential Pipeline to gather info in parallel, then synthesize ---
root_agent = SequentialAgent(
    name="city_insights_root_agent",
    description="Takes a user query about a city and returns weather, travel tip, and history.",
    sub_agents=[parallel_insight_agent, summary_agent],
)