from google.adk.agents import LlmAgent
from blog_writer.config import GEMINI_MODEL

planner = LlmAgent(
    name="planner",
    model=GEMINI_MODEL,
    description="Creates a practical, skimmable outline in Markdown.",
    instruction="""
You are the planning specialist.

Your ONLY responsibility is to create a blog outline.
Do NOT write the article.
Do NOT explain the sections.
Do NOT generate any blog content beyond the outline.

Create a Markdown outline with:
- Title
- Short introduction
- 4–6 main sections with 2–3 bullets each
- Conclusion

Return ONLY the outline.
""",
    output_key="blog_outline",
)
