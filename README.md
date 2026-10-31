# Elevvo Python Programming & AI

A collection of Python automation and AI projects developed for the Elevvo Python Programming & AI internship. The four projects cover file organization, weather API integration, document question answering, and AI-assisted code review. Each task folder contains its own source code, documentation, and setup instructions.

## Projects

| Task | Project | Level | Status | Demo |
| --- | --- | --- | --- | --- |
| 3 | [Automated File Organizer](task-03-file-organizer/) | Level 2 | Complete | [Play demo](#task-3-demo) |
| 5 | [Weather Dashboard Using a Public REST API](task-05-weather-dashboard/) | Level 3 | Complete | [Play Demo](#task-5-demo) |
| 7 | [LLM-Powered Document Q&A Tool](task-07-document-qa/) | Industry Level | Complete | [Play Demo](#task-7-demo) |
| 8 | [AI-Assisted Code Review Tool](task-08-code-reviewer/) | Industry Level | Complete | [Play Demo](#task-8-demo) |

The file organizer groups files by extension, handles duplicate names, and supports logging and dry-run previews. The weather dashboard retrieves current conditions for a chosen city, supports Celsius and Fahrenheit, handles request failures, and includes automated tests with mocked API responses.

The document Q&A tool answers questions from five sample recipe documents, cites the retrieved source chunks, and declines questions when no chunk meets its configured relevance threshold. It includes both a command-line interface and a Gradio web interface. The code review tool produces structured findings for bugs, PEP 8 compliance, and refactoring, validates the report, and previews proposed edits in a diff before the user accepts or rejects them.

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

Run each project from its own task directory. The file organizer uses Python's standard library. The weather dashboard uses `requests` and `python-dotenv`, with `pytest` for its automated tests; its setup instructions explain how to configure a WeatherAPI key in a local `.env` file.

The document Q&A tool uses local SentenceTransformer embeddings, a persistent Chroma vector store, and the OpenAI API for answers. Follow its README to configure `OPENAI_API_KEY`, prepare the sample document index, and launch either the CLI or the Gradio app.

The code review tool uses the OpenAI API, Pydantic report models, and `python-dotenv` configuration. Follow its README to install dependencies from `requirements.txt`, configure `OPENAI_API_KEY`, select a Python file, and review the proposed changes before choosing whether to save them.

## Documentation and demos

Each task README describes its requirements, bonuses, setup, example usage, and demo. [README_GUIDE.md](README_GUIDE.md) defines the repository's documentation conventions.

### Task 3 demo

The recording shows dry-run and normal modes, duplicate filename handling, existing subfolders, and log output.

https://github.com/user-attachments/assets/389521a6-e81c-48fc-8df9-9a1bcd7d1927

### Task 5 demo

The recording demonstrates Cairo and Riyadh weather lookup, Celsius and Fahrenheit output, an invalid city, and the mocked API tests.

https://github.com/user-attachments/assets/bc1b7e92-8d66-4bca-aeac-a4e3b7e09686

### Task 7 demo

The recording demonstrates the project running in both the command-line and Gradio web interfaces. Each interface is used to ask questions relevant to the recipe documents and unrelated questions, showing answers with source filenames and full supporting chunks for relevant questions, and the refusal message for unrelated questions.

https://github.com/user-attachments/assets/c08f2b9e-1b1e-4eb0-9ecb-901c850abe44

### Task 8 demo

The recording demonstrates reviewing the supplied sample file, displaying structured findings, inspecting the before/after diff and proposed code, rejecting changes with `N`, and accepting changes with `Y`.

https://github.com/user-attachments/assets/9d99fe3a-887d-470e-9192-e9c6b26581f8

## Author

Bushra Magdy
