# Elevvo Python Programming & AI

A collection of Python automation and AI projects developed for the Elevvo Python Programming & AI internship. The projects cover file organization, weather API integration, document question answering, AI-assisted code review, and a two-tool AI agent. Each task folder contains its own source code, documentation, and setup instructions.

## Projects

| Task | Project | Level | Status | Demo |
| --- | --- | --- | --- | --- |
| 3 | [Automated File Organizer](task-03-file-organizer/) | Level 2 | Complete | [Play demo](#task-3-demo) |
| 5 | [Weather Dashboard Using a Public REST API](task-05-weather-dashboard/) | Level 3 | Complete | [Play Demo](#task-5-demo) |
| 7 | [LLM-Powered Document Q&A Tool](task-07-document-qa/) | Industry Level | Complete | `TASK_7_DEMO_URL` |
| 8 | [AI-Assisted Code Review Tool](task-08-code-reviewer/) | Industry Level | Complete | `TASK_8_DEMO_URL` |
| 9 | [AI Agent for a Two-Tool Task](task-09-two-tool-agent/) | Industry Level | Complete | `TASK_9_DEMO_URL` |

The file organizer groups files by extension, handles duplicate names, and supports logging and dry-run previews. The weather dashboard retrieves current conditions for a chosen city, supports Celsius and Fahrenheit, handles request failures, and includes automated tests with mocked API responses.

The AI projects provide answers grounded in supplied documents, code-review suggestions, and an agent workflow that uses two tools to complete a goal. See each project's README for its requirements, configuration, usage, and design decisions.

## Getting started

Clone the repository:

```sh
git clone https://github.com/bushramagdy3/elevvo-python-ai.git
cd elevvo-python-ai
```

Choose a project and follow its setup instructions:

- [Task 3: Automated File Organizer](task-03-file-organizer/README.md#setup)
- [Task 5: Weather Dashboard Using a Public REST API](task-05-weather-dashboard/README.md#setup)
- [Task 7: LLM-Powered Document Q&A Tool](task-07-document-qa/README.md#setup)
- [Task 8: AI-Assisted Code Review Tool](task-08-code-reviewer/README.md#setup)
- [Task 9: AI Agent for a Two-Tool Task](task-09-two-tool-agent/README.md#setup)

Run each project from its own task directory. The file organizer uses Python's standard library. The weather dashboard uses `requests` and `python-dotenv`, with `pytest` for its automated tests; its setup instructions explain how to configure a WeatherAPI key in a local `.env` file.

## Documentation and demos

Each task README describes its requirements, bonuses, setup, example usage, demo, testing, and limitations. [README_GUIDE.md](README_GUIDE.md) defines the repository's documentation conventions.

### Task 3 demo

The recording shows dry-run and normal modes, duplicate filename handling, existing subfolders, and log output.

https://github.com/user-attachments/assets/389521a6-e81c-48fc-8df9-9a1bcd7d1927

### Task 5 demo

The recording demonstrates Cairo and Riyadh weather lookup, Celsius and Fahrenheit output, an invalid city, and the mocked API tests.

https://github.com/user-attachments/assets/bc1b7e92-8d66-4bca-aeac-a4e3b7e09686

## Author

Bushra Magdy — [GitHub](https://github.com/bushramagdy3).
