from pydantic import BaseModel

class AgentConfig(BaseModel):
    agent_name: str
    agent_role: str
    agent_goal: str
    agent_backstory: str

class TaskConfig(BaseModel):
    task_name: str
    task_description: str
    task_output: str
    task_agent: str