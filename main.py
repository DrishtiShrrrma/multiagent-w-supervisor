from workflow.workflow_graph import workflow

def main():
    print("Starting Workflow...")
    initial_message = "Analyze the GDP data for trends."
    for step in workflow.stream({"messages": [initial_message]}):
        if "__end__" not in step:
            print(step)
            print("----")

if __name__ == "__main__":
    main()
