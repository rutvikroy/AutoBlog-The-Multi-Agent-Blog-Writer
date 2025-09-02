from llmProject.entity.config_entity import AgentConfig, TaskConfig
from llmProject.constants import AGENTS_FILE_PATH, TASKS_FILE_PATH
from llmProject.utils.common import read_yaml

class ConfigurationManager:
    def __init__(self, agents_file_path=AGENTS_FILE_PATH, tasks_file_path=TASKS_FILE_PATH):
        self.agents_config = read_yaml(agents_file_path)
        self.tasks_config = read_yaml(tasks_file_path)

    def get_research_agent_config(self) -> AgentConfig:
        research_agent = AgentConfig(
            agent_name="researcher_agent",
            agent_role=self.agents_config.researcher_agent.role,
            agent_goal=self.agents_config.researcher_agent.goal,
            agent_backstory=self.agents_config.researcher_agent.backstory
        )
        return research_agent
    
    def get_reporting_agent_config(self) -> AgentConfig:
        reporting_agent = AgentConfig(
            agent_name="reporting_agent",
            agent_role=self.agents_config.reporting_agent.role,
            agent_goal=self.agents_config.reporting_agent.goal,
            agent_backstory=self.agents_config.reporting_agent.backstory
        )
        return reporting_agent

    def get_editor_agent_config(self) -> AgentConfig:
        editor_agent = AgentConfig(
            agent_name="editor_agent",
            agent_role=self.agents_config.editor_agent.role,
            agent_goal=self.agents_config.editor_agent.goal,
            agent_backstory=self.agents_config.editor_agent.backstory
        )
        return editor_agent
    
    def get_research_task_config(self) -> TaskConfig:
        research_task = TaskConfig(
            task_name="research_task",
            task_description=self.tasks_config.research_task.description,
            task_output=self.tasks_config.research_task.expected_output,
            task_agent=self.tasks_config.research_task.agent
        )
        return research_task
    
    def get_report_task_config(self) -> TaskConfig:
        research_task = TaskConfig(
            task_name="report_task",
            task_description=self.tasks_config.report_task.description,
            task_output=self.tasks_config.report_task.expected_output,
            task_agent=self.tasks_config.report_task.agent
        )
        return research_task
    
    def get_edit_task_config(self) -> TaskConfig:
        research_task = TaskConfig(
            task_name="edit_task",
            task_description=self.tasks_config.edit_task.description,
            task_output=self.tasks_config.edit_task.expected_output,
            task_agent=self.tasks_config.edit_task.agent
        )
        return research_task
