from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents import AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st

ASSISTANT_ID = "asst_6MfY2bV0tjC7aPZPYxABZSna"

agent = OpenAIAssistantRunnable(assistant_id=ASSISTANT_ID, as_agent=True)
agent_executor = AgentExecutor(agent=agent, tools=[], verbose=False)

history = []

# initiate agent and therad
# get system langauge, time and location
import time
TIME = None
init_prompt = """
THIS IS AN ADDITIONAL INSTRUCTION PROMPT, YOU ARE NOT TALKING TO THE USER YET.
===
Here is additional information about the clients system:
- System Language: English
- System Time: 10:45 AM
===
You are A sales executive at YOE, specializing in online electric vehicle sales and customer guidance.
"""
init_response = agent_executor.invoke({
    "content": init_prompt
})
thread_id = init_response['thread_id']


while True:
    user_input = input("You: ")
    if user_input == "exit":
        break

    response = agent_executor.invoke(
        {
            "content": user_input,
            "thread_id": thread_id
        }
    )

    print("AI: ", response["output"])
