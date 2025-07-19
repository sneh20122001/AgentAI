from config import TAVILY_API_KEY, GROQ_API_KEY
import os 
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool
import asyncio 

os.environ['GROQ_API_KEY'] = GROQ_API_KEY

agent = Agent(
    'groq:llama-3.1-8b-instant',
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt="Search Tavily for the given query and return the results."
)

async def get_search_query(query: str):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, agent.run_sync, query)
    return result.output