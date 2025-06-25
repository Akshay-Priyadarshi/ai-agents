# AI Agents with ADK: Example Collection

This repository contains a collection of example projects demonstrating how to build, extend, and deploy AI agents using the Agent Development Kit (ADK) and related SDKs (A2A, MCP, Google ADK, etc.).

## What is ADK?

The Agent Development Kit (ADK) is a framework for building intelligent agents powered by Large Language Models (LLMs). ADK agents can reason, use tools, maintain state, and interact with users or other agents. This repo showcases practical patterns for:

- Stateless and stateful agents
- Tool-using agents (web search, code execution, custom functions)
- Structured output with Pydantic
- Persistent storage (SQLite, production DBs)
- Agent-to-agent (A2A) communication
- Integrations (e.g., Notion)

## Progressive Example Agents & Tools

This repository is organized as a learning journey. Each numbered folder introduces new ADK agent concepts, tools, and integrations, building on the previous example. Follow them in order for a smooth progression from basics to advanced topics:

---

### 1. [1-basic-agent/](./1-basic-agent)

**Agent:** `greeting_agent`

- **What you'll learn:** The absolute basics of an ADK agent. This agent simply greets the user and asks for their name, showing how to define an LLM-powered agent with a simple instruction.
- **Next step:** Once you understand agent structure and LLM instructions, move to tool integration.
- **Docs:** [ADK LLM Agent](https://google.github.io/adk-docs/agents/llm-agent/)

---

### 2. [2-tool-agent/](./2-tool-agent)

**Agent:** `tool_agent`

- **What you'll learn:** How to give your agent superpowers with built-in tools like Google Search. You'll see how to add tools to your agent and how the LLM can use them to answer more complex queries.
- **Next step:** After learning tool integration, try enforcing structured outputs for more reliable downstream use.
- **Docs:** [ADK Tools](https://google.github.io/adk-docs/tools/), [Google Search Tool](https://google.github.io/adk-docs/tools/built-in-tools/#google-search)

---

### 3. [3-structured-output/](./3-structured-output)

**Agent:** `email_agent`

- **What you'll learn:** How to make your agent return structured data (not just text!) using Pydantic models and ADK's `output_schema`. This is essential for integrating agents with other systems.
- **Next step:** Now that you can control output, learn how to make your agent remember things across turns with session state.
- **Docs:** [Structured Output in ADK](https://google.github.io/adk-docs/agents/llm-agent/#structured-output), [Pydantic](https://docs.pydantic.dev/)

---

### 4. [4-sessions-and-state/](./4-sessions-and-state)

**Agent:** `question_answering_agent`

- **What you'll learn:** How to maintain session state and personalize responses. This agent remembers user info and uses it to answer questions, showing how to use template variables and state.
- **Next step:** Ready for real-world use? Add persistent storage so your agent remembers users even after a restart.
- **Docs:** [Sessions in ADK](https://google.github.io/adk-docs/sessions/session/), [State Management](https://google.github.io/adk-docs/sessions/state/)

---

### 5. [5-persistent-storage/](./5-persistent-storage)

**Agent:** `reminder_agent`

- **What you'll learn:** How to give your agent long-term memory using persistent storage (SQLite). This agent manages reminders and demonstrates custom tools for CRUD operations, all with data that survives restarts.
- **Next step:** Explore integrations with external APIs and multi-agent systems.
- **Docs:** [Persistent Storage in ADK](https://google.github.io/adk-docs/sessions/session/#persistent-storage)

---

### 6. [6-mcp-agent/](./6-mcp-agent)

**Agent:** `Notion_MCP_Agent`

- **What you'll learn:** How to connect your agent to external services (like Notion) using the Model Context Protocol (MCP). This agent can automate and interact with Notion workspaces.
- **Next step:** Try agent-to-agent communication for distributed, collaborative AI systems.
- **Docs:** [Notion API](https://developers.notion.com/docs/mcp), [MCP Protocol](https://github.com/modelcontextprotocol/servers)

---

### 7. [7-a2a-agent/](./7-a2a-agent)

**Agent:** `Greeting Agent` (A2A)

- **What you'll learn:** The basics of agent-to-agent (A2A) communication using the A2A Python SDK. This example shows how agents can expose skills, communicate, and collaborate.
- **Next step:** Combine these patterns to build your own advanced, multi-agent, tool-using, persistent AI systems!
- **Docs:** [A2A SDK](https://github.com/google/a2a-python), [A2A Concepts](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge#1)

---

Each subfolder contains its own README with usage instructions and more details. Progress through them in order for the best learning experience!

## Setup

- **Python**: Requires Python 3.13+
- **Virtual Environment**: Recommended (see below)
- **Dependencies**: Managed with [uv](https://docs.astral.sh/uv/) and `pyproject.toml`/`uv.lock`

### 1. Create and activate a virtual environment

```bash
uv venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
uv pip install -r uv.lock
```

### 3. Set up API keys

- Most examples require a Google API key for Gemini models. Copy `.env.example` to `.env` in the relevant example folder and add your key:
  ```
  GOOGLE_API_KEY=your_api_key_here
  ```

## Quickstart: Run the Basic Agent Example

```bash
cd 1-basic-agent
adk web
```

- Open the provided URL (usually http://localhost:8000)
- Select your agent and start chatting!

## More Examples

- See each subdirectory's README for details, usage, and troubleshooting.
- Try the persistent storage, tool agent, and A2A agent for more advanced patterns.

## Resources

- [ADK Documentation](https://google.github.io/adk-docs/)
- [A2A Python SDK](https://github.com/google/a2a-python)
- [ADK Tools Guide](https://google.github.io/adk-docs/tools/)
- [Session & State Management](https://google.github.io/adk-docs/sessions/session/)

---

**Contributions and issues welcome!**
