from google.adk.agents import LoopAgent

from blog_writer.agents.planner import planner
from blog_writer.agents.outline_validator import outline_validator

robust_planner = LoopAgent(
    name="robust_planner",
    description="Generates and validates a blog outline until it passes validation.",
    sub_agents=[
        planner,
        outline_validator,
    ],
    max_iterations=3,
)
