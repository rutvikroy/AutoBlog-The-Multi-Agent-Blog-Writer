from llmProject import logger
from llmProject.config.configuration import ConfigurationManager


STAGE_NAME = "Config Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    config_manager = ConfigurationManager()

    logger.info(f">>>>  Reseach Task  <<<<\n\nx===")
    research_task = config_manager.get_research_task_config()
    print("Task name: ", research_task.task_name)
    print("Task description: ",research_task.task_description)
    print("Task output: ",research_task.task_output)
    print("Task agent: ",research_task.task_agent)

    logger.info(f">>>>  Reseach Agent  <<<<\n\nx===")
    research_agent = config_manager.get_research_agent_config()
    print("Agent name: ", research_agent.agent_name)
    print("Agent role: ",research_agent.agent_role)
    print("Agent goal: ",research_agent.agent_goal)
    print("Agent backstory: ",research_agent.agent_backstory)

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
