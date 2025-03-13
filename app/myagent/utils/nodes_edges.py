#Nodes functions for the graph
import uuid
from .state import OverallState
from langchain_core.runnables import RunnableConfig,RunnableLambda
from langgraph.store.base import BaseStore
from .configuration import Configuration as conf
from .models import Models
from . import tools
from . import prompts
from langchain_core.messages import SystemMessage, HumanMessage,ToolMessage
from langgraph.prebuilt import ToolNode


#Basic Agent: 
#In init we have the state, the configuration, and the store that represents the long-term memory of our Agent.
#We gonna prepare a model with example tools for this template.
tool_s = [tools.UpdateMemory,tools.add, tools.multiply, tools.divide]
model_with_tools = Models.get_model("gpt-4o-mini").bind_tools(tool_s, parallel_tool_calls=False)


def call_agent(state: OverallState, config: RunnableConfig, store: BaseStore):
    #In configuration.py we have make the configuration object for our agent. But,
    #we are in LCEL, so we have to use the Runnable Interface, so we create a RunnableConfig
    #object with our schema in configuration.py.
    configurable = config["configurable"]
    user_id =configurable.get("user_id","1")
    #Reminder: The memory in langgraph is a key-value store defined by namespaces (tuple).
    namespace = ("memories", user_id)
    memories = store.search(namespace)
    sys_prompt = prompts.EXAMPLE_SYS_PROMPT.format(memories=memories)
    response = model_with_tools.invoke([SystemMessage(content=sys_prompt)] + state["messages"])
    return {"messages":[response]}

#---Tool Nodes: Prebuilt
def handle_tool_error(state: OverallState) -> dict:
    """
    Maneja errores de herramientas en el flujo de trabajo del grafo.

    :param state: El state debe contener por lo menos:
                  - "messages": Una lista de mensajes, donde el último mensaje será la respuesta de la toolcall, el cual será
                  el error.
    :return: En vez de parar la ejecución,  empaquetamos este error en un ToolMessage para mandarselo al agente.
    """
    tool_calls = state["messages"][-1].tool_calls
    return {
        "messages": [
            ToolMessage(
                content=f"Error: please fix your mistakes.",
                tool_call_id=tc["id"],
            )
            for tc in tool_calls
        ]
    }


def create_tool_node_with_fallback(tools: list) -> dict:
    """
    Crea un nodo con una lista de herramientas y agrega fallbacks
    para manejar errores en caso de fallos durante la ejecución.
    :param tools: Una lista de herramientas (tools) que se asignarán al nodo.
    :return: Un nodo de herramientas capaz de iterar entre fallbacks para corregirlos
    """
    return ToolNode(tools).with_fallbacks(
        [RunnableLambda(handle_tool_error)], exception_key="error"
    )


