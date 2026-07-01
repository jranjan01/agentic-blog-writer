# 🤖 Multi-Agent Technical Blog Writer

An AI-powered multi-agent blog generation system built with **Python**, **Google ADK**, and **Gemini**.

The application uses specialized AI agents that collaborate to generate high-quality technical blog posts. Instead of relying on a single LLM prompt, the system separates responsibilities into planning, writing, and validation agents, making the workflow modular, extensible, and easier to maintain.

---

## Features

- Multi-agent architecture using Google ADK
- Dedicated Planner, Writer, and Validator agents
- Intelligent workflow coordination
- Automatic blog outline generation
- Technical blog generation in Markdown
- Shared agent state using `output_key`
- Retry-based validation workflow using `LoopAgent`
- Environment-based configuration using `.env`
- Dependency management with UV

---

## Architecture

```text
                    User
                      │
                      ▼
               Blogger (Coordinator)
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
   Robust Planner            Robust Writer
     (LoopAgent)              (LoopAgent)
         │                         │
   ┌─────┴─────┐             ┌─────┴─────┐
   ▼           ▼             ▼           ▼
 Planner   Validator      Writer    Validator
```

---

## Technologies

- Python 3.13
- Google ADK
- Gemini API
- UV
- dotenv

---

## Workflow

1. User provides a blog topic.
2. The coordinator agent delegates planning to the planner workflow.
3. The planner creates a structured Markdown outline.
4. The outline is validated.
5. The writer generates the complete technical blog.
6. The generated article is validated.
7. The final Markdown article is returned.

---

## Running the Project

### Clone the repository

```bash
git clone <repo-url>
cd agentic-blog-writer
```

### Install dependencies

```bash
uv sync
```

### Configure environment

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.5-flash
GEMENI_LITE_MODEL=gemini-2.5-flash-lite
```

### Start ADK Web

```bash
uv run adk web
```
### Lint

```bash
uv run ruff format .
```


### Flow

```text
User
 │
 │ "Write a blog on URL Shortener"
 ▼
blogger
 │
 ▼
robust_planner
 │
 ├── planner
 │       │
 │       ▼
 │  Creates outline
 │
 └── outline_validator
         │
         ▼
      OK?
      │
      ├── Yes
      └── No → planner again
 │
 ▼
robust_writer
 │
 ├── writer
 │       │
 │       ▼
 │  Writes complete blog
 │
 └── post_validator
         │
         ▼
      OK?
      │
      ├── Yes
      └── No → writer again
 │
 ▼
Final Blog
```