import json
import os
from pathlib import Path

from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# ---- MCP Library ----
# https://github.com/modelcontextprotocol/servers
# https://smithery.ai/

# ---- Notion -----
# https://developers.notion.com/docs/mcp
# https://github.com/makenotion/notion-mcp-server
# https://github.com/makenotion/notion-mcp-server/blob/main/scripts/notion-openapi.json



NOTION_API_KEY = os.getenv("NOTION_API_KEY")
if NOTION_API_KEY is None:
    raise ValueError("NOTION_API_KEY is not set")

NOTION_MCP_HEADERS = json.dumps(
    {"Authorization": f"Bearer {NOTION_API_KEY}", "Notion-Version": "2022-06-28"}
)

# Read the prompt from prompt.md
def get_system_prompt():
    prompt_path = Path(__file__).parent / "prompt.md"
    with open(prompt_path, "r") as f:
        return f.read()
    
SYSTEM_PROMPT = get_system_prompt()

root_agent = Agent(
    model="gemini-2.0-flash",
    name="Notion_MCP_Agent",
    instruction=SYSTEM_PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "@notionhq/notion-mcp-server"],
                env={"OPENAPI_MCP_HEADERS": NOTION_MCP_HEADERS},
            )
        ),
    ],
)