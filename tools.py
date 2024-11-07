from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.tools import PythonREPLTool
from langchain_community.tools.pandas_data_tool import PandasDataTool
from langchain_community.tools.google_translate_tool import GoogleTranslateTool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from vectorstore import retriever  # Import retriever from vectorstore.py

# Define individual tools
tavily_tool = TavilySearchResults(max_results=5)
python_repl_tool = PythonREPLTool()
data_analysis_tool = PandasDataTool()
translator_tool = GoogleTranslateTool(target_language="en")

# Define RAG Tool function
def RAG(state):
    question = state
    template = "Answer the question based only on the following context:\n{context}\n\nQuestion: {question}"
    
    prompt = ChatPromptTemplate.from_template(template)
    retrieval_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | ChatOpenAI()
    )
    return retrieval_chain.invoke(question)
