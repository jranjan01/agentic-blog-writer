from google.adk.agents import LlmAgent

from blog_writer.agents.robust_planner import robust_planner
from blog_writer.agents.robust_writer import robust_writer
from blog_writer.config import GEMINI_MODEL


blogger = LlmAgent(
    name="blogger",
    model=GEMINI_MODEL,
    description="Coordinates planning, writing, and validation to generate technical blog posts.",
    instruction="""
You are an AI Technical Blog Coordinator.

Your responsibility is to coordinate the blog generation workflow by delegating tasks to the appropriate sub-agents.

When the user's request is to generate a technical blog or article, coordinate the workflow by delegating work to the appropriate sub-agents.

Responsibilities:
- Understand the user's request.
- Delegate planning tasks to the sub-agent 'robust_planner'.
- After planning completes successfully, delegate writing tasks to the sub-agent 'robust_writer'.
- Return only the final validated Markdown article.

Guidelines:
- Never generate an outline yourself.
- Never write or rewrite the article yourself.
- Do not expose intermediate outputs such as outlines or validation results.
- If the workflow cannot produce a valid blog after all retry attempts, clearly explain what failed and suggest that the user refine the topic or try again.
""",
    sub_agents=[
        robust_planner,
        robust_writer,
    ],
)


# Note: If you're using the free trial of Gemini 2.5 Flash, use the code below. It helps avoid daily usage limit errors and other common issues.

# from google.adk.agents import SequentialAgent

# from blog_writer.agents.planner import planner
# from blog_writer.agents.writer import writer

# blogger = SequentialAgent(
#     name="blogger",
#     description="Technical blog generation pipeline.",
#     sub_agents=[
#         planner,
#         writer,
#     ],
# )
