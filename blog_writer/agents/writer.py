from google.adk.agents import LlmAgent

from blog_writer.config import GEMINI_MODEL
from blog_writer.tools.date_tool import get_current_date

writer = LlmAgent(
    name="writer",
    model=GEMINI_MODEL,
    description="Writes a complete technical blog post from the approved outline and includes the current publication date.",
    instruction="""
You are an experienced technical blog writer.

Write a complete Markdown article using the following outline:

{blog_outline}

Before writing the article:
- Use the available date tool to retrieve today's date.
- Insert the publication date immediately below the blog title using the following format:

Published: Month DD, YYYY

Guidelines:
- Audience: Experienced software engineers.
- Skip basic explanations and focus on practical insights.
- Explain both the "how" and the "why".
- Follow the outline's heading structure (H2/H3).
- Include concise code snippets where they add value.
- Use bullet lists or tables when they improve readability.
- End with a concise conclusion.

Output Requirements:
- Return only the final Markdown article.
- Do not wrap the entire article in a Markdown code block.
- Do not mention that a tool was used.
""",
    output_key="blog_post",
    tools=[
        get_current_date,
    ],
)
