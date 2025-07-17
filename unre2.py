from crewai import Agent
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-4", temperature=0.3)

dev_agent = Agent(
    role="Python Dev",
    goal="Fetch top CPU usage on the system",
    backstory="Experienced SRE automation engineer",
    llm=llm
)


from crewai import Task

task1 = Task(
    description="Get list of top 5 CPU-consuming processes on a Windows machine.",
    expected_output="A list of process names and CPU usage",
    agent=dev_agent
)


from crewai import Crew

crew = Crew(agents=[dev_agent], tasks=[task1], verbose=True)
result = crew.kickoff()
print(result)