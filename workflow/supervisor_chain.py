from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Define the available agents and their roles
members = ["RAG", "Researcher", "Coder", "DataAnalyst", "Translator"]
options = ["FINISH"] + members

# Define the supervisor system prompt
system_prompt = (
    "You are a supervisor tasked with managing a conversation between the following workers: {members}."
    " Based on the conversation, decide who should act next or if the task is complete (FINISH)."
    " Use the RAG tool for questions related to Japan or Sports."
)

# Define the function for routing decisions
function_def = {
    "name": "route",
    "description": "Select the next agent or conclude the task.",
    "parameters": {
        "title": "routeSchema",
        "type": "object",
        "properties": {
            "next": {
                "title": "Next",
                "anyOf": [
                    {"enum": options},
                ],
            }
        },
        "required": ["next"],
    },
}

# Setup the supervisor chain prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        (
            "system",
            "Who should act next, or should we FINISH? Select from: {options}"
        ),
    ]
).partial(options=str(options), members=", ".join(members))

# Compile the supervisor chain
supervisor_chain = (
    prompt
    | ChatOpenAI(model="gpt-4-1106-preview").bind_functions(functions=[function_def], function_call="route")
    | JsonOutputFunctionsParser()
)
