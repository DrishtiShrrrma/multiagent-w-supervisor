# **Multi-Agent Workflow System with Supervisor Node**

The **Multi-Agent Workflow System with Supervisor Node** is a modular, task-oriented framework designed to handle complex workflows by dynamically routing tasks to specialized agents. Each agent, such as the RAG (Retrieval-Augmented Generation) agent, code generator, data analyst, and translator, is equipped with specific tools and capabilities to efficiently manage designated tasks. A central supervisor node orchestrates agent interactions, ensuring that each query is accurately processed through the appropriate agents until completion. The project includes both a command-line interface (CLI) and a Streamlit web app for user interaction.

## Table of Contents

- [Features](#features)
- [Tools and Models Used](#tools-and-models-used)
- [Workflow Diagram](#workflow-diagram)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Running the CLI](#running-the-cli)
  - [Running the Streamlit Web App](#running-the-streamlit-web-app)
- [Future Enhancements](#future-enhancements)
- [Additional Notes](#additional-notes)

---

## Features

- **Supervisor-Driven Workflow Management**: A supervisor node dynamically routes tasks to the relevant agents, assessing each query type to continue processing or conclude the workflow.
- **Specialized Task Agents**: Task-specific agents are configured with distinct tools and functions, such as web search, code execution, data analysis, and translation, to ensure accurate task management.
- **Streamlined Tool Integration**: Integrates specialized tools for retrieval-augmented generation (RAG), Python code execution, data analysis, and language translation to support a variety of query types.
- **Multi-Interface Support**: Offers both a command-line interface (CLI) and a Streamlit web app for convenient user interaction.
- **Context-Aware Processing**: The supervisor evaluates task context to determine agent routing, allowing efficient and contextually relevant handling of complex workflows.

---

## Tools and Models Used

- **Programming Language**: Python
- **Key Libraries**:
  - **LangChain**: Manages agent workflows and supervises dynamic decision-making.
  - **LangChain Community Tools**: Provides additional tools for specialized tasks, including translation and data analysis.
  - **Chroma**: Implements a vector-based database for document retrieval.
  - **HuggingFace BGE**: Supplies embeddings for document retrieval and similarity scoring in the RAG setup.
- **Language Model**:
  - **OpenAI GPT-4**: Provides responses based on agent prompts and interacts with tools via LangChain integrations.

---

## Workflow Diagram

The following diagram outlines the workflow for processing user queries. Each task is dynamically routed through relevant agents, guided by the supervisor node, which evaluates task context and routes queries to appropriate agents.

```plaintext
User Query -> Supervisor -> Task Agent(s) (e.g., Research, RAG, Coding) -> Supervisor -> Completion or Further Processing
```


<img width="528" alt="image" src="https://github.com/user-attachments/assets/f35e6bc7-2c15-4826-886c-003b2f90054f">

---

## Project Structure

Here’s an overview of the project’s structure:

```
Multi-Agent Workflow System/
│
├── agents.py               # Defines agent configurations and initialization functions
├── tools.py                # Contains tool definitions and setup for each task-specific tool
├── vectorstore.py          # Sets up document loading, embeddings, and vector database for RAG
├── workflow/               # Manages the workflow graph and supervisor chain
│   ├── __init__.py         # Makes this directory a package
│   ├── workflow_graph.py   # Constructs the workflow graph and agent routing
│   └── supervisor_chain.py # Contains supervisor logic for agent routing and task conclusion
├── data/                   # Stores data-related files
│   └── source/             # Directory for source documents to load into vector DB
│       └── *.txt           # Text files for document retrieval in RAG
├── config/                 # Configuration files
│   └── settings.py         # API keys and other configuration (optional)
├── main.py                 # Command-line interface for running the workflow
├── streamlit_app.py        # Streamlit web app for interactive user queries
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/multi-agent-workflow-system.git
cd multi-agent-workflow-system
```

### Step 2: Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up API Keys

Set up your API keys as environment variables in `config/settings.py` or directly in `main.py`:

```python
import os
os.environ['OPENAI_API_KEY'] = "your_openai_api_key"
```

Alternatively, use a `.env` file for secure management of API keys.

---

## Usage

### Running the CLI

To start the workflow system using the CLI:

```bash
python main.py
```

After starting, the CLI will prompt you to input queries. Each query will initiate the workflow, and the supervisor node will route tasks to appropriate agents. You can type `exit` to end the session.

### Running the Streamlit Web App

To interact with the workflow system via a web-based interface:

```bash
streamlit run streamlit_app.py
```

This command will launch the Streamlit app, accessible at `http://localhost:8501`. Enter your query in the input box, and click "Submit" to see real-time responses as tasks progress through the workflow.

---

## Workflow Description

### Task Routing with the Supervisor Node

The Supervisor Node acts as the central routing mechanism, determining the appropriate agent for each task based on query context:

1. **Initialization**: The supervisor receives the query and evaluates it against task categories.
2. **Agent Routing**: The supervisor selects the appropriate agent(s) for each part of the task (e.g., RAG for retrieval tasks, Coder for code generation).
3. **Dynamic Progression**: Once an agent completes its task, the supervisor assesses the next step, either routing the task to another agent or finishing the workflow.

### Example Scenarios

1. **Code Generation Task**:
   - Input: "Generate Python code to print 'Hello, World!'"
   - Expected Workflow: Supervisor → Coder Agent → Supervisor → Completion

2. **RAG Retrieval Task**:
   - Input: "What is Japan's GDP over the last 4 years?"
   - Expected Workflow: Supervisor → RAG Agent → Supervisor → Completion

3. **Data Analysis Task**:
   - Input: "Analyze GDP data trends and create a graph."
   - Expected Workflow: Supervisor → RAG Agent → Data Analysis Agent → Coder Agent → Supervisor → Completion

These scenarios demonstrate the supervisor’s role in routing tasks dynamically for comprehensive workflow management.

---

## Future Enhancements

- **Enhanced Task Context Analysis**: Develop more granular task analysis to improve routing accuracy for complex, multi-step queries.
- **Expanded Agent Capabilities**: Integrate additional agents with specialized tools for fields like finance, healthcare, and education.
- **Multilingual Processing**: Extend language support for multilingual workflows, allowing for non-English queries.
- **Session-Based Memory**: Implement memory within sessions, allowing the system to retain context across multiple related queries.







sample queries (India): 

1. "What are the primary factors behind India's industrial growth in 2024?"
2. "How is India planning to meet its renewable energy goals by 2030?"
3. "What has been the impact of India hosting the Cricket World Cup on the local economy?"
4. "How has India's sports industry evolved, particularly in badminton and eSports?"
5. "What are India’s main exports in 2024, and how is the rupee’s exchange rate impacting trade?"

sample queries (cricket):

1. "How has the Women’s IPL impacted the growth of cricket among young girls in India?"
2. "What were the main factors contributing to India’s revenue growth in cricket in 2024?"
3. "Which players have made the biggest impact in international cricket for India since 2020?"
4. "How has technology influenced the decision-making and analytics in Indian cricket?"
5. "What are the viewership trends for IPL in the last five years, and how does it compare to other sports leagues globally?"






