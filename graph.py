from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint import MemorySaver
from langgraph.prebuilt import create_react_agent

from azure_tool import AzureCliTool

load_dotenv()

memory = MemorySaver()
model = ChatOpenAI(model="gpt-4o", temperature=0)

graph = create_react_agent(model, tools=[AzureCliTool()], checkpointer=memory)
