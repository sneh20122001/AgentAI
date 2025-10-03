import os
from crewai import Crew
from decouple import config
from textwrap import dedent
from agent import CustomAgents
from tasks import JobTrendTasks

os.environ["GEMINI_API_KEY"] = config("GEMINI_API_KEY")

class CustomCrew:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        # Initialize agents and tasks
        agents = CustomAgents()
        tasks = JobTrendTasks()

        # Get agents
        custom_agent_1 = agents.agent_1_name()
        custom_agent_2 = agents.agent_2_name()

        # Get tasks - these already include the agents internally
        custom_task_1 = tasks.gather_job_data()
        custom_task_2 = tasks.analyze_trends()

        # Create the crew
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2],
            verbose=True,
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter variable 1: """))
    var2 = input(dedent("""Enter variable 2: """))

    custom_crew = CustomCrew(var1, var2)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)
