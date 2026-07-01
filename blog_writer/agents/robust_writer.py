from google.adk.agents import LoopAgent

from blog_writer.agents.writer import writer
from blog_writer.agents.post_validator import post_validator

robust_writer = LoopAgent(
    name="robust_writer",
    description="Retries blog writing until validation succeeds.",
    sub_agents=[
        writer,
        post_validator,
    ],
    max_iterations=3,
)
