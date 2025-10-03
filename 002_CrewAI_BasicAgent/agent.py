# custom_agents.py

from crewai import Agent, LLM
from textwrap import dedent

class CustomAgents:

    def __init__(self):
        self.Geminiflash = LLM(model="gemini/gemini-2.0-flash", temperature=0.7)
        self.Geminiflash2 = LLM(model="gemini/gemini-2.0-flash", temperature=0.9)

    def agent_1_name(self):
        return Agent(
            role="Tech Job Market Researcher",
            backstory=dedent("""
                An expert tech industry researcher who specializes in analyzing job market platforms and labor reports.
                They are highly skilled in identifying current hiring trends and surfacing critical data from reliable sources.
            """),
            goal=dedent("""
                To gather comprehensive and up-to-date information about the current tech job market and industry shifts.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.Geminiflash,
        )

    def agent_2_name(self):
        return Agent(
            role="Tech Workforce Analyst",
            backstory=dedent("""
                A strategic analyst focused on interpreting job market data and deriving actionable insights for professionals and companies.
            """),
            goal=dedent("""
                To provide a concise, insightful analysis of tech job trends and offer career strategy suggestions.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.Geminiflash2,
        )
