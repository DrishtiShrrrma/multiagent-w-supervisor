**Start: Multi-Agent Query Processing System**
|
|--> **User Input Handling**
|    |
|    |--> Receive User Query
|    |--> Send Query to **Supervisor Node**
|    |--> **Output**: Directed to appropriate agent based on query type
|
|--> **Supervisor Node**
|    |
|    |--> Evaluate Query Content and Type
|         |
|         |-- **If query is about Japan or sports** --> Direct to **RAG Node**
|         |
|         |-- **If query involves data/code** --> Direct to **Coder Node**
|         |
|         |-- **If query involves research** --> Direct to **Researcher Node**
|    |
|    |--> **Output**: Agent Selection Decision
|
|--> **Agent Nodes**
|    |
|    |--> **RAG Node** (for Japan and Sports Queries)
|    |    |
|    |    |--> Retrieve relevant information using Retrieval-Augmented Generation (RAG)
|    |    |--> Process with Chroma vector database and embeddings
|    |    |--> Generate response using context-based prompt
|    |    |--> Return Result to Supervisor
|    |
|    |--> **Coder Node** (for Code/Data Queries)
|    |    |
|    |    |--> Execute Python code or data analysis using PythonREPLTool
|    |    |--> Generate safe code to meet user request
|    |    |--> Return Result to Supervisor
|    |
|    |--> **Researcher Node** (for General Research Queries)
|         |
|         |--> Conduct web-based search using Tavily Search tool
|         |--> Return search results to Supervisor
|
|--> **Supervisor - Completion Check**
|    |
|    |--> Evaluate Results from Agent Nodes
|    |    |
|    |    |--> **If further processing needed** --> Route back to appropriate Agent Node
|    |    |
|    |    |--> **If all tasks complete** --> Mark as FINISH
|    |
|    |--> **Output**: Final consolidated response or loop to Agent Node
|
|--> **Final Output Generation**
|    |
|    |--> Consolidate and format responses from all agents
|    |--> Provide Final Answer to User
|
|--> **End: Multi-Agent Query Processing System Completed**

