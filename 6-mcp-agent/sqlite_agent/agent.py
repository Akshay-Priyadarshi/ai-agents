from pathlib import Path

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

from mcp_servers.sqlite import get_script_path

SCRIPT_PATH = get_script_path()

# Read the prompt from prompt.md
def get_system_prompt():
    prompt_path = Path(__file__).parent / "prompt.md"
    with open(prompt_path, "r") as f:
        return f.read()
    
SYSTEM_PROMPT = get_system_prompt()

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="sqlite_agent",
    instruction=SYSTEM_PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="python3",
                args=[SCRIPT_PATH],
            )
            # tool_filter=['list_tables'] # Optional: ensure only specific tools are loaded
        )
    ],
)