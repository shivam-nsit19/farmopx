
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from config import config_list

# === Create Agents ===

soil_agent = AssistantAgent(
    name="SoilTestingAgent",
    llm_config={"config_list": config_list, "temperature": 0},
    system_message="You are an expert soil testing agent. Analyze soil samples and return structured results."
)

land_agent = AssistantAgent(
    name="LandOptimizationAgent",
    llm_config={"config_list": config_list, "temperature": 0},
    system_message="You are a land optimization agent. Provide land usage suggestions based on soil data."
)

critic_agent = AssistantAgent(
    name="CriticAgent",
    llm_config={"config_list": config_list, "temperature": 0},
    system_message="You are a critic agent that evaluates suggestions and provides feedback or improvements."
)

user_proxy = UserProxyAgent(
    name="UserProxyAgent",
    code_execution_config=False  # Set to True if you want code execution
)

# === Group Chat Setup ===

group_chat = GroupChat(
    agents=[user_proxy, soil_agent, land_agent, critic_agent],
    messages=[],
    max_round=10
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list": config_list}
)

# === Start the Task ===

