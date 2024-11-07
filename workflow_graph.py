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

# Define conditional edges and routing logic
workflow.add_edge("Researcher", "Supervisor")
workflow.add_edge("RAG", "Supervisor")
# Add other edges and set entry point
workflow.set_entry_point("Supervisor")
