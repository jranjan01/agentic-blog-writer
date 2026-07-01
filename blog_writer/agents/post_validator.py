from google.adk.agents import LlmAgent
from blog_writer.config import GEMENI_LITE_MODEL

post_validator = LlmAgent(
    name="post_validator",
    model=GEMENI_LITE_MODEL,
    description="Validates the final blog post.",
    instruction="""
Review the following blog post:

{blog_post}

Check that it includes:
- An introduction
- Clear sections that follow the outline
- Technical accuracy and clarity
- Practical insights
- A conclusion

If the article passes all checks, respond exactly:

ok

Otherwise respond exactly:

retry

Then briefly list the specific issues to fix.
""",
    output_key="validation_result",
)
