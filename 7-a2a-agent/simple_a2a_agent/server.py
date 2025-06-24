import uvicorn
from utils import get_a2a_app, get_a2a_request_handler
from .agent_executer import GreetingAgentExecutor
from .agent import agent_card
from a2a.server.tasks import InMemoryTaskStore


def main():
    a2a_request_handler = get_a2a_request_handler(GreetingAgentExecutor(),InMemoryTaskStore())
    a2a_app = get_a2a_app(a2a_request_handler,agent_card)
    uvicorn.run(a2a_app.build(), host="0.0.0.0", port=9999)

if __name__ == "__main__":
    main()