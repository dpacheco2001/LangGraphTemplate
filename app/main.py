from trustcall import create_extractor
from langchain_openai import ChatOpenAI
class Spy:
    def __init__(self):
        self.called_tools = []

    def __call__(self, run):
        q = [run]
        while q:
            r = q.pop()
            if r.child_runs:
                q.extend(r.child_runs)
            if r.run_type == "chat_model":
                self.called_tools.append(
                    r.outputs["generations"][0][0]["message"]["kwargs"]["tool_calls"]
                )
spy = Spy()


model = ChatOpenAI(model="gpt-4o-mini", temperature=0)


trustcall_extractor = create_extractor(
    model,
    tools=[Memory],
    tool_choice="Memory",
    enable_inserts=True,
)
trustcall_extractor_see_all_tool_calls = trustcall_extractor.with_listeners(on_end=spy)