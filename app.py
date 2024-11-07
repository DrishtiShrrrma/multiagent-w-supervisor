import streamlit as st
from workflow.workflow_graph import workflow
from langchain_core.messages import HumanMessage

# Streamlit App Title
st.title("Agent Workflow System")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input box
user_input = st.text_input("Enter your query:", placeholder="e.g., Fetch Japan's GDP over the last 4 years and draw a line graph.")

# Submit button
if st.button("Submit"):
    if user_input:
        # Append user input as a message in the session state
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        # Initialize workflow with the user's input
        st.write("### Workflow Execution:")
        for step in workflow.stream({"messages": st.session_state.messages}):
            if "__end__" in step:
                st.write("**Workflow completed.**")
                break
            else:
                st.write(step)  # Display each agent’s response in the workflow
                st.write("----")
                
        # Clear input after submission
        user_input = ""
    else:
        st.warning("Please enter a query before submitting.")

# Display conversation history
st.write("### Conversation History:")
for message in st.session_state.messages:
    st.write(message.content)
