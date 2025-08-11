from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

summary_agent = LlmAgent(
    name="summary_agent",
    model=GEMINI_MODEL,
    instruction="""You are a summarizer.

    You will be given:
    - weather_info
    - travel_tip
    - history_fact
    
    Combine all three into a short report:
    ---
    Weather: ...
    Travel Tip: ...
    History: ...
    ---
    
    Be clear and concise. Do not invent or modify data.
    """,
    description="Combines weather, travel tip, and historical fact into a single output.",
    output_key="final_summary"
)