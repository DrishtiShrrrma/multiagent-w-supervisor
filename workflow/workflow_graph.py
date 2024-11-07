from langgraph.graph import StateGraph, END
from agents import research_agent, code_agent, rag_agent, data_analysis_agent, translation_agent, agent_node
from workflow.supervisor_chain import supervisor_chain
import functools

# Initialize the workflow graph
workflow = StateGraph()
workflow.add_node("Researcher", functools.partial(agent_node, agent=research_agent, name="Researcher"))
workflow.add_node("Coder", functools.partial(agent_node, agent=code_agent, name="Coder"))
workflow.add_node("RAG", functools.partial(agent_node, agent=rag_agent, name="RAG"))
workflow.add_node("DataAnalyst", functools.partial(agent_node, agent=data_analysis_agent, name="DataAnalyst"))
workflow.add_node("Translator", functools.partial(agent_node, agent=translation_agent, name="Translator"))
workflow.add_node("Supervisor", supervisor_chain)

# Define routing logic
for member in ["Researcher", "Coder", "RAG", "DataAnalyst", "Translator"]:
    workflow.add_edge(member, "Supervisor")  # Route each agent back to supervisor after their task

# Supervisor decides the next agent or finishes
conditional_map = {k: k for k in ["Researcher", "Coder", "RAG", "DataAnalyst", "Translator"]}
conditional_map["FINISH"] = END
workflow.add_conditional_edges("Supervisor", lambda x: x["next"], conditional_map)

# Set entry point for workflow
workflow.set_entry_point("Supervisor")
