from myagent.graph import compilegraph
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore
from langchain_core.messages import HumanMessage


config = {"configurable": {"thread_id": 1, "user_id": "1"}}
memory = MemorySaver()
long_term_memory = InMemoryStore()

template_graph= compilegraph(checkpointer=memory,long_term_memory=long_term_memory)

while True:
    inp=input("Enter a message: ")
    if inp=="exit":
        break
    if inp == "see_memory":
        print(long_term_memory.search(("memories","1")))
        continue
    response=template_graph.invoke({"messages":HumanMessage(content=inp)},config)
    print("Human: ",inp)
    print("Assistant: ",response["messages"][-1].content)
