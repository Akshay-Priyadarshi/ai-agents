from a2a.server.request_handlers import RequestHandler, DefaultRequestHandler
from a2a.server.agent_execution import AgentExecutor
from a2a.server.apps import A2AStarletteApplication, JSONRPCApplication
from a2a.server.tasks import TaskStore
from a2a.types import AgentCard

def get_a2a_request_handler(agent_executer: AgentExecutor, task_store: TaskStore) -> RequestHandler:
    return DefaultRequestHandler(
        agent_executor=agent_executer,
        task_store=task_store,
    )

def get_a2a_app(request_handler: RequestHandler, agent_card: AgentCard) -> JSONRPCApplication:
    return A2AStarletteApplication(
        http_handler=request_handler,
        agent_card=agent_card,
    )



