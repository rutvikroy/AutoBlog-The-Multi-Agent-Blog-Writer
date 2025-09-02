from llmProject import logger
from llmProject.config.configuration import ConfigurationManager
from crewai import Agent, Task, Crew, LLM


STAGE_NAME = "Config Ingestion"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    config_manager = ConfigurationManager()

    logger.info(f">>>>  Reseach Task  <<<<\n\nx===")
    research_task_config = config_manager.get_research_task_config()
    print("Task name: ", research_task_config.task_name)
    print("Task description: ",research_task_config.task_description)
    print("Task output: ",research_task_config.task_output)
    print("Task agent: ",research_task_config.task_agent)

    logger.info(f">>>>  Reseach Agent  <<<<\n\nx===")
    research_agent_config = config_manager.get_research_agent_config()
    print("Agent name: ", research_agent_config.agent_name)
    print("Agent role: ",research_agent_config.agent_role)
    print("Agent goal: ",research_agent_config.agent_goal)
    print("Agent backstory: ",research_agent_config.agent_backstory)

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Create Agents"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    
    llm = LLM(model="gemini/gemini-2.0-flash",temperature=0.7)
    research_agent_config = config_manager.get_research_agent_config()
    reporting_agent_config = config_manager.get_reporting_agent_config()
    editor_agent_config = config_manager.get_editor_agent_config()

    reseach_agent = Agent(
        role=research_agent_config.agent_role,
        goal=research_agent_config.agent_goal,
        backstory=research_agent_config.agent_backstory,
        llm=llm,
        allow_delegation=False,
        verbose=True
    )
    
    reporting_agent = Agent(
        role=reporting_agent_config.agent_role,
        goal=reporting_agent_config.agent_goal,
        backstory=reporting_agent_config.agent_backstory,
        llm=llm,
        allow_delegation=False,
        verbose=True
    )
    
    editor_agent = Agent(
        role=editor_agent_config.agent_role,
        goal=editor_agent_config.agent_goal,
        backstory=editor_agent_config.agent_backstory,
        llm=llm,
        allow_delegation=False,
        verbose=True
    )


    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Create Tasks"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    research_task_config = config_manager.get_research_task_config()
    report_task_config = config_manager.get_report_task_config()
    edit_task_config = config_manager.get_edit_task_config()

    research_task = Task(
        description=research_task_config.task_description,
        expected_output=research_task_config.task_output,
        agent=reseach_agent, 
    )

    report_task = Task(
        description=report_task_config.task_description,
        expected_output=report_task_config.task_output,
        agent=reporting_agent, 
    )
    
    edit_task = Task(
        description=edit_task_config.task_description,
        expected_output=edit_task_config.task_output,
        agent=editor_agent, 
    )

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Create Crew"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    crew = Crew(
        agents=[reseach_agent, reporting_agent, editor_agent],
        tasks=[research_task, report_task, edit_task],
        verbose=False 
    )

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e