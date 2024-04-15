from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from streamlit_chat import message
import yaml
from langchain.agents import AgentExecutor
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st

ASSISTANT_ID = "asst_6MfY2bV0tjC7aPZPYxABZSna"

agent = OpenAIAssistantRunnable(assistant_id=ASSISTANT_ID,
                                as_agent=True)
agent_executor = AgentExecutor(agent=agent,
                               tools=[],
                               verbose=False)
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

@st.cache_resource()
def init_(init_prompt):
    init_response = agent_executor.invoke({
        "content": init_prompt
    })
    return init_response

# spinner
with st.spinner('Your agent is pouring himself a cup of coffee, please wait a moment...'):
    init_response = init_(init_prompt)
thread_id = init_response['thread_id']


with open("./assistant/company.yaml", "r") as f:
    company = yaml.load(f, Loader=yaml.FullLoader)

st.title(company["name"] + " - Sales Representative")

st.sidebar.image(company["logo"], use_column_width=True)
st.sidebar.title("Company Information")
st.sidebar.markdown(f"{company['mission']}")
st.sidebar.markdown(f"**Headquarters:** {company['headquarters']}")
st.sidebar.markdown(f"**Website:** [{company['website']}]({company['website']})")

import time
if "messages" not in st.session_state:
    st.session_state.messages = []
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

if prompt := st.chat_input("You"):
    # append user message to messages
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = agent_executor.invoke({
        "content": prompt,
        "thread_id": thread_id,
    })
    st.chat_message("agent").write(response['output'], markdown=False)
    st.session_state.messages.append({"role": "agent", "content": response['output']})
