from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from tools import tavily_tool, python_repl_tool, data_analysis_tool, translator_tool, RAG
from langchain_core.messages import HumanMessage

# Common agent creation function
def create_agent(llm: ChatOpenAI, tools: list, system_prompt: str):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    agent = create_openai_tools_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools)

llm = ChatOpenAI(model="gpt-4-1106-preview")

research_agent = create_agent(llm, [tavily_tool], "You are a web researcher.")
code_agent = create_agent(llm, [python_repl_tool], "Generate safe Python code for analysis.")
rag_agent = create_agent(llm, [RAG], "Use this tool for questions on Japan or sports.")
data_analysis_agent = create_agent(llm, [data_analysis_tool], "Perform data analysis tasks.")
translation_agent = create_agent(llm, [translator_tool], "Translate foreign content.")

# Agent node function for workflow integration
def agent_node(state, agent, name):
    result = agent.invoke(state)
    return {"messages": [HumanMessage(content=result["output"], name=name)]}
