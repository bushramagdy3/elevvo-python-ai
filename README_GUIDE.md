# README Writing Guide — Elevvo Python Programming & AI

## Instructions for the coding AI

Read this guide before creating or updating any README in this repository. Follow it for the root README and for every task README. This is the repository owner's documentation convention, not an official Elevvo grading rubric.

Inspect the actual code, dependency files, tests, and available demo assets first. Document only implemented behaviour. Never invent features, successful test results, performance numbers, links, awards, or completion status. Do not implement extra features merely to fill a documentation section.

## Repository organization

Repository name: `elevvo-python-ai`.

Use these task folders for the agreed project selection:

| Task | Folder | Title | Level |
| --- | --- | --- | --- |
| 3 | `task-03-file-organizer/` | Automated File Organizer | Level 2 |
| 5 | `task-05-weather-dashboard/` | Weather Dashboard Using a Public REST API | Level 3 |
| 7 | `task-07-document-qa/` | LLM-Powered Document Q&A Tool | Industry Level |
| 8 | `task-08-code-reviewer/` | AI-Assisted Code Review Tool | Industry Level |
| 9 | `task-09-two-tool-agent/` | AI Agent for a Two-Tool Task | Industry Level |

Each task has its own README, source code, dependency declaration, and sample inputs where needed. Keep tests in that task's `tests/` folder and screenshots in `assets/` when applicable. Adapt source layout to the actual implementation; do not create empty folders for appearance. Preserve an established working layout and update links if it differs from these defaults.

## Root README: use this order

### 1. Title and introduction

Title: `Elevvo Python Programming & AI`.

Use this introductory description, adjusting tense only when supported by actual progress:

> A collection of Python automation and AI projects developed for the Elevvo Python Programming & AI internship. The selected projects cover file organization, weather API integration, document question answering, AI-assisted code review, and a two-tool AI agent. Each task folder contains its own documentation and setup instructions.

### 2. Projects

Use one table with columns: Task, Project, Level, Status, Demo. Link each project to its folder. Use `Planned`, `In progress`, or `Complete` honestly. A planned folder or missing demo must appear as plain text rather than a broken link. Write `Not recorded yet` for a missing demo.

### 3. Getting started

Explain how to clone the repository and choose a task. Link to each task's setup instructions. Do not imply there is one command that launches all five projects unless that command exists. Use verified repository URLs only.

### 4. Documentation and demos

Explain that each task README contains its requirements coverage, setup, usage, demo, tests, and limitations. Keep this paragraph short.

### 5. Author

Author: Bushra Magdy. GitHub: https://github.com/bushramagdy3.

Add acknowledgments for reused code or resources when applicable. Add a license section only if a license has actually been selected and included.

## Every task README: use this exact order

### 1. Title and overview

Use `Task N — Project Name` as the title. State the level and explain the program's purpose in two or three sentences. Describe the actual interface: CLI, web app, or script. Do not describe a CLI as a web dashboard.

### 2. Requirements coverage

Create a table with columns `Required feature`, `Implementation`, and `Status`. Map the official task requirements to concrete behaviour and relevant relative code links. Use `Complete`, `Partial`, or `Not implemented` honestly. Consult the supplied task PDF; if it is unavailable, flag that the mapping needs verification instead of inventing its contents.

### 3. Bonuses and additional features

Separate official bonuses from the author's own additions. List only implemented items. Explicitly mark any remaining official bonus as incomplete. Do not call a core requirement a bonus.

### 4. Setup

Include the tested Python version if known, the task directory to run commands from, virtual environment instructions, dependency installation, and required configuration. Use copyable fenced shell commands that match the real files. Do not invent entry points or dependency filenames.

For API/model configuration, list environment variable names and their purpose. Provide `.env.example` with placeholders if the application uses environment variables. Never include real credentials. Explain any API account, paid service, model download, or external dependency needed to run the project. Include Windows activation instructions alongside macOS/Linux when using a virtual environment.

### 5. Usage

Provide the exact launch command and one complete sample interaction, including input and expected output. Label illustrative output as illustrative. Explain relevant arguments or controls briefly. For file-moving tools, use a disposable sample directory for examples.

### 6. Demo

Link one roughly 60–90 second recording showing normal operation, a handled error or edge case, and an implemented bonus where practical. Use a verified hosted video link or a relative link to an actual recording. A screenshot may provide a preview, but do not assume Markdown can play a local MP4 inline.

If the recording is unavailable, write `Demo not recorded yet` and include a short recording checklist. Never fabricate a URL or imply a recording exists.

An error demonstration means giving a working program invalid input or a difficult situation and showing its correct response. Do not deliberately break the implementation, reveal credentials, or cause destructive changes to record a failure.

### 7. Tests and evaluation

Include the actual test command and the important behaviours covered. State results only if the tests were run, and identify the scope of the run. If tests could not run, state the reason. Avoid unsupported coverage percentages.

For AI projects, also show a small evaluation table with input, expected behaviour, observed result, and pass/fail. Include successful and failure cases; do not report only favourable examples. Distinguish tests with mocked model/API responses from live integration checks.

### 8. Design decisions and limitations

Briefly explain the main processing steps, one or two meaningful implementation choices, and practical limitations. Mention relevant network dependencies, model uncertainty, supported formats, and cost or execution limits. Keep this specific to the project.

### 9. Attribution

Credit reused components, tutorials, models, data, or substantial external code when applicable. Disclose reused work from earlier projects and what was newly developed for this task. Omit this section if there is nothing to attribute; do not invent sources.

## Demo and evaluation cases by task

| Task | Normal case | Error or edge case to demonstrate |
| --- | --- | --- |
| 3 — File organizer | Sort a disposable sample folder by extension | An incoming file conflicts with an existing destination filename; both remain intact |
| 5 — Weather | Retrieve Cairo weather | A nonexistent city receives a helpful response; test timeouts with a mock |
| 7 — Document Q&A | Answer a question from sample documents and cite the supporting chunks | An unrelated question falls below the configured retrieval threshold and is declined |
| 8 — Code reviewer | Produce a structured review of a deliberately buggy sample file | A missing input file is handled clearly; test malformed model output separately |
| 9 — Two-tool agent | Complete and log a goal using the two configured tools | A tool failure is handled; verify that the execution limit stops an unfinished run |

For Task 7, report the actual threshold and scoring method. For Task 8, explain report validation and approximate line references, and document that suggestions are not automatically executed or applied. For Task 9, name the two tools and execution limit; log tool inputs and outputs without exposing hidden model reasoning. If implementing the third-tool bonus, document the default two-tool mode and the optional third-tool mode clearly.

## Final documentation checks

- All relative links and referenced files exist; missing items are marked honestly.
- Commands match the implementation and specify the correct working directory.
- Core requirements, official bonuses, and personal additions are distinguished.
- Screenshots and recordings use safe sample data and contain no secrets.
- Completion, test, and evaluation claims match evidence.
- The root project table agrees with each task README.
- Keep the language concise and factual. Avoid decorative badges, exaggerated claims, repeated boilerplate, and claims of official recognition that has not been awarded.

## Short GitHub repository description

Python automation and AI projects for the Elevvo internship: file organization, weather APIs, document Q&A, code review, and a two-tool AI agent.
