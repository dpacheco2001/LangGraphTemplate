#Tools for the graph
from typing import Annotated, Literal, TypedDict
import uuid
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from langgraph.store.base import BaseStore
from langgraph.prebuilt import InjectedStore
#Example tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b


#This will be a different kind of tool, this will help us to update the memory of the agent, but not here,but in the a node in the graph.
#This will make the llm make a toolcall with the argument we want.
@tool
def UpdateMemory(memory: str, config: RunnableConfig, store: Annotated[BaseStore, InjectedStore()])-> dict:

    """Reflect on the chat history and update the memory collection."""

    configurable =  config["configurable"]
    user_id = configurable["user_id"]
    namespace = ("memories", user_id)
    store.put(namespace,str(uuid.uuid4()),memory)
    return "Memory updated en espacio de nombres: "+str(namespace)

