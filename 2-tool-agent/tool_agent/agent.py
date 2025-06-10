from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool Agent",
    tools=[google_search],
    instruction="""
    You are a helpful assistant, and you have access
    to the following tools.
    - google_search
    """
)