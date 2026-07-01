from google.adk.agents import LlmAgent
from blog_writer.config import GEMENI_LITE_MODEL

outline_validator = LlmAgent(
    name="outline_validator",
    model=GEMENI_LITE_MODEL,
    description="Validates that the outline is usable.",
    instruction="""
Review the following blog outline:

{blog_outline}

The outline must contain:
- A clear title
- An introduction
- 4 to 6 main sections
- A conclusion

If it satisfies all requirements, respond exactly:

ok

Otherwise respond exactly:

retry

Then briefly list the missing or incorrect items.
""",
    output_key="validation_result",
)
