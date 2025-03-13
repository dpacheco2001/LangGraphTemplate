#Code and logic for graph compilation
from .utils.state import OverallState
from .utils.nodes_edges import call_agent, create_tool_node_with_fallback,tool_s
from langgraph.graph import StateGraph, MessagesState, END, START

from langgraph.prebuilt import tools_condition



builder = StateGraph(OverallState)
builder.add_node(call_agent)
builder.add_node("tools", create_tool_node_with_fallback(tool_s))
builder.add_edge(START, "call_agent")
builder.add_conditional_edges(
    "call_agent",
    tools_condition,
)
builder.add_edge("tools", "call_agent")



def compilegraph(checkpointer=None,long_term_memory=None):
    return builder.compile(checkpointer=checkpointer,store=long_term_memory)