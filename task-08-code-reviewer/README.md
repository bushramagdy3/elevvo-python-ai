# Task 8 — AI-Assisted Code Review Tool

**Level:** Industry Level

**Status:** Complete

A command-line tool that reviews an existing Python file using the OpenAI API. It produces structured findings for bugs, PEP 8 compliance, and refactoring, validates the report, and marks unverified line references as approximate. The CLI lists issues and suggestions for human review.

## Requirements coverage

| Required feature | Implementation | Status |
| --- | --- | --- |
| Read an existing Python file and request bug detection, PEP 8 review, and refactoring suggestions | [main.py](main.py) reads the bundled `python-files/incorrect_sample.py` and sends its source to `gpt-4o` with a structured review prompt. | Complete |
| Parse the response into a structured report with issue, line, and suggestion fields | Pydantic `Issue` and `Response` models define the report, including the original snippet and approximate-line flag. | Complete |
| Validate required fields and reject entries with invalid or empty values | Pydantic validates required fields and their types. `validateResponse()` rejects nonpositive line numbers and blank descriptions, suggestions, or source snippets. | Complete |
| Mark line references as approximate when they cannot be verified against the file | `validateLineAndSnippt()` compares the snippet with the original source line, including exact indentation and whitespace. Unverified findings are marked approximate. | Complete |
| Review and report suggestions without automatically executing or applying generated changes | The program prints a structured report. It does not execute the reviewed code or write changes to the input file. | Complete |

## Sample inputs

[python-files/incorrect_sample.py](python-files/incorrect_sample.py) and [python-files/correct_sample.py](python-files/correct_sample.py) provide sample review inputs.

## Setup

Use Python 3.14. Local verification used Python 3.14.6. An OpenAI API key and access to the configured `gpt-4o` model are required. API requests require an internet connection and are subject to account limits and usage charges.

Run the following from the repository root.

Windows PowerShell:

```powershell
cd task-08-code-reviewer
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```sh
cd task-08-code-reviewer
python3 -m venv .venv
source .venv/bin/activate
```

Install the runtime dependencies from [requirements.txt](requirements.txt) in the active virtual environment:

```sh
python -m pip install -r requirements.txt
```

### API configuration

Create a `.env` file beside `main.py`, using [.env.example](.env.example) as a template:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
```

| Setting | Purpose |
| --- | --- |
| `OPENAI_API_KEY` | Authenticates code-review requests to the OpenAI API. |

The application reads this file with `python-dotenv`. Start the script from `task-08-code-reviewer` so the configuration file is found. Local `.env` files are excluded from version control. The source file is sent to the OpenAI API for review.

## Usage

From the task directory with the virtual environment active:

```sh
python main.py
```

The script reviews `python-files/incorrect_sample.py` by default. To review another file, change the `path` assignment in the `__main__` block of [main.py](main.py).

The CLI prints a `Response` containing the issues, original code snippets, line numbers, approximate-line flags, and suggestions. All findings remain in the report, including approximate references.

Illustrative output for a one-line file containing `total=0`; generated findings and suggested wording can vary:

```text
issues=[Issue(issue='PEP 8: Missing spaces around the assignment operator.', code_snippet='total=0', line=1, line_approximate=False, suggestion='Add spaces around the assignment operator.')]
```

Review the suggestions and make any desired changes in your editor.

## Demo

Demo not recorded yet for the review-only version.

**Limitation:** AI suggestions may be incomplete or incorrect. Line verification checks only the source reference; it does not establish that a finding or suggestion is correct.
