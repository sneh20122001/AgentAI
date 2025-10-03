# job_trend_tasks.py

from crewai import Task
from textwrap import dedent
from agent import CustomAgents  

class JobTrendTasks:
    def __init__(self):
        self.tip = "Use the most accurate and up-to-date sources. Think like a market analyst."
        self.agents = CustomAgents()  # Initialize custom agents

    def gather_job_data(self):
        return Task(
            description=dedent(f"""
                Task 1: Gather Current Job Trends in Tech

                Research the most recent data on job trends in the tech industry.
                Include:
                - Top in-demand tech roles (e.g., Data Scientist, DevOps Engineer)
                - Most requested skills (e.g., Python, AWS, Docker, AI/ML)
                - Notable industry shifts (e.g., increase in remote roles, layoffs, or hiring spikes)
                - Data sources: LinkedIn, Indeed, Glassdoor, or industry reports

                {self.tip}

                Make the output structured and clear.
            """),
            expected_output="A structured report listing current tech job trends with sources.",
            agent=self.agents.agent_1_name(),  # Use agent 1
        )

    def analyze_trends(self):
        return Task(
            description=dedent(f"""
                Task 2: Analyze Tech Job Trend Data

                Using the output from Task 1, provide an analysis that includes:
                - Which roles are growing fastest
                - Which skills are in highest demand
                - Observations on remote vs in-office demand
                - Any geographical trends (if applicable)
                - Career suggestions based on these trends

                {self.tip}

                Be insightful and concise. Include charts if possible.
            """),
            expected_output="An analytical summary of tech job trends with strategic insights.",
            agent=self.agents.agent_2_name(),  # Use agent 2
        )
