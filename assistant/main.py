from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import yaml
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
# spinner
with st.spinner('Your agent is pouring himself a cup of coffee, please wait a moment...'):
    init_response = agent_executor.invoke({
        "content": init_prompt
    })
print("Your agent is pouring himself a cup of coffee, please wait a moment...")
thread_id = init_response['thread_id']


with open("company.yaml", "r") as f:
    company = yaml.load(f, Loader=yaml.FullLoader)

st.title(company["name"])

st.sidebar.image(company["logo"], use_column_width=True)
st.sidebar.title("Company Information")
st.sidebar.markdown(f"{company['mission']}")
st.sidebar.markdown(f"**Headquarters:** {company['headquarters']}")
st.sidebar.markdown(f"**Website:** [{company['website']}]({company['website']})")
