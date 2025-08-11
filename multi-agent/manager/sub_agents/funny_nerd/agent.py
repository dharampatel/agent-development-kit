from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def get_nerd_joke(topic: str, tool_context: ToolContext) -> dict:
    """Get a nerdy joke about a specific topic."""
    print(f"--- Tool: get_nerd_joke called for topic: {topic} ---")

    # Example jokes - in a real implementation, you might want to use an API
    jokes = {
        "python": "Why don't Python programmers like to use inheritance? Because they don't like to inherit anything!",
        "javascript": "Why did the JavaScript developer go broke? Because he used up all his cache!",
        "java": "Why do Java developers wear glasses? Because they can't C#!",
        "programming": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "math": "Why was the equal sign so humble? Because he knew he wasn't less than or greater than anyone else!",
        "physics": "Why did the photon check a hotel? Because it was travelling light!",
        "chemistry": "Why did the acid go to the gym? To become a buffer solution!",
        "biology": "Why did the cell go to therapy? Because it had too many issues!",
        "default": "Why did the computer go to the doctor? Because it had a virus!",
    }

    joke = jokes.get(topic.lower(), jokes["default"])

    # Update state with the last joke topic
    tool_context.state["last_joke_topic"] = topic

    return {"status": "success", "joke": joke, "topic": topic}


# Create the funny nerd agent
funny_nerd = Agent(
    name="funny_nerd",
    model="gemini-2.0-flash",
    description="An agent that tells nerdy jokes about various topics.",
    instruction="""
    
    You are a funny nerd agent who tells nerdy jokes across technical and scientific topics.

    When asked to tell a joke:
    1. Use the get_nerd_joke tool with the requested topic.
    2. If no topic is mentioned, ask: "What kind of nerdy joke would you like? (e.g., Python, math, physics, etc.)"
    3. Format the response with the joke and a brief explanation if needed.
    
    Available topics include:
        - python
        - javascript
        - java
        - programming
        - math
        - physics
        - chemistry
        - biology
    
        Example response format:
        "Here's a nerdy joke about <TOPIC>:
        <JOKE>
    
        Explanation: {brief explanation if needed}"
    
    If the user's request is unrelated to nerdy jokes or unclear:
    - Do NOT reply directly.
    - Return control to the manager to handle it.
    """,
    tools=[get_nerd_joke],
)