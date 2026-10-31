# Task 8 — AI-Assisted Code Review Tool

**Level:** Industry Level

**Status:** Complete

A command-line tool that reviews an existing Python file using the OpenAI API. It produces structured findings for bugs, PEP 8 compliance, and refactoring, validates the report, and marks unverified line references as approximate. The CLI displays the findings, a before/after diff, and the proposed code, with explicit approval required before saving changes.

## Requirements coverage

| Required feature | Implementation | Status |
| --- | --- | --- |
| Read an existing Python file and request bug detection, PEP 8 review, and refactoring suggestions | [main.py](main.py) reads the selected file and sends its source to `gpt-4o` with a structured review prompt. | Complete |
| Parse the response into a structured report with issue, line, and suggestion fields | Pydantic `Issue` and `Response` models define the report, including the original snippet, suggested code, action type, and approximate-line flag. | Complete |
| Validate required fields and reject entries with invalid or empty values | Pydantic validates required fields and their types. `validateResponse()` rejects nonpositive line numbers and blank descriptions, suggestions, source snippets, or suggested code. | Complete |
| Mark line references as approximate when they cannot be verified against the file | `validateLineAndSnippt()` compares the snippet with the reported source line, ignoring surrounding whitespace. Unverified findings are marked approximate and excluded from proposed edits. | Complete |
| Review and report suggestions without automatically executing or applying generated changes | The program displays its report and preview without executing the reviewed code. The input file is overwritten only after the user explicitly enters `Y`. | Complete |

## Bonuses and additional features

**Official bonus — Before/after diff with manual acceptance or rejection: Complete.** The CLI marks original lines with `-` and suggested lines with `+`, displays the proposed file contents, and asks whether to save the changes. Entering `Y` accepts the proposed edits; any other response leaves the file unchanged.

Additional features:

- Duplicate line references are filtered so the first valid issue for each line is retained.
- Replacement edits preserve the original line's indentation and use the first line of suggested code.
- Insertion actions support adding multiple lines before or after a targeted line.
- [python-files/incorrect_sample.py](python-files/incorrect_sample.py) and [python-files/correct_sample.py](python-files/correct_sample.py) provide sample review inputs.

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

The application reads this file with `python-dotenv`. Start the script from `task-08-code-reviewer` so the configuration file is found. Local `.env` files are excluded from version control. The selected source file is sent to the OpenAI API for review.

## Usage

From the task directory with the virtual environment active:

```sh
python main.py
```

Enter the path of the Python file when prompted, for example `python-files/incorrect_sample.py`. You can enter an absolute path or a path relative to the current task directory.

The CLI displays `Issues`, the `Before and after diff`, and the proposed `New Code`. Approximate findings remain in the report but are skipped when building the proposed edits.

Illustrative output after entering the path of a one-line file containing `total=0`; generated findings and suggested wording can vary:

```text
Issues:
[Issue(issue='PEP 8: Missing spaces around the assignment operator.', code_snippet='total=0', line=1, line_approximate=False, suggestion='Add spaces around the assignment operator.', suggested_code='total = 0', action_type='replace_line')]
Before and after diff:
- total=0
+ total = 0
New Code:
total = 0
Would you like to apply these changes? (Y/N) N
```

Enter `Y` to overwrite the selected input file with the proposed code. The choice ignores letter case and surrounding whitespace. Enter `N`, or any other response, to keep the original file. The reviewed code is never executed by the tool.

## Demo

The recording demonstrates reviewing the supplied sample file, displaying structured findings, inspecting the before/after diff and proposed code, rejecting changes with `N`, and accepting changes with `Y`.

Demo video: `TASK_8_DEMO_URL`

**Limitation:** AI suggestions may be incomplete or incorrect, especially renames and refactors involving several lines. Review the diff before accepting; the proposed code is not executed or checked for correctness.
