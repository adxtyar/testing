from crewai import Agent, Task, Crew
from langchain.llms import OpenAI

# 1. Setup your LLM (you can use any you have access to)
llm = OpenAI(model="gpt-4", temperature=0.3)

# 2. Create a meta-agent that will generate CrewAI code
crew_builder_agent = Agent(
    role="CrewAI Code Generator",
    goal="Generate Python CrewAI scripts from natural language use cases",
    backstory=(
        "You are an expert in automating workflows using CrewAI and Python."
        " Given any use case described in plain English, you generate ready-to-run Python code that sets up agents, tasks, crew, and any needed logic like API calls."
    ),
    llm=llm
)

# 3. Example task for this agent
use_case = (
"""
I want an automation that runs on my local machine. It should:

1. Use Python to collect current system performance data like CPU usage, memory usage, disk usage, and the top 5 running processes.
2. Save this data into a `.log` file inside a folder named `logs/`. The log file should be named using the current timestamp.
3. Then, the system should read all existing `.log` files in the `logs/` folder.
4. It should analyze the logs and summarize trends such as average CPU usage, peak memory usage, most frequent high-CPU process, etc.
5. Finally, it should save this summary into a file called `summary_report.txt` in the root project folder.

The entire workflow should be implemented using CrewAI with separate agents handling system monitoring, logging, parsing logs, summarizing data, and generating the final report.
"""
)

meta_task = Task(
    description=f"Write full CrewAI Python code to handle this use case: {use_case}",
    expected_output="A complete runnable Python script including agent setup, tasks, crew kickoff, and Microsoft Graph API integration.",
    agent=crew_builder_agent
)

# 4. Create a Crew with this single agent and task
meta_crew = Crew(
    agents=[crew_builder_agent],
    tasks=[meta_task],
    verbose=True  # So you see the full output
)

# 5. Run the meta-agent
result = meta_crew.kickoff()

# 6. Save the result to a Python script
with open("generated_crew_script.py", "w") as f:
    f.write(result)

print("✅ CrewAI script has been generated and saved as 'generated_crew_script.py'")
