# Task 8 — AI-Assisted Code Review Tool

**Level:** Industry Level

**Status:** Complete

A command-line tool that reviews an existing Python file using the OpenAI API. It produces structured findings for bugs, PEP 8 compliance, and refactoring, validates the report, and marks unverified line references as approximate. The CLI lists issues and suggestions, asks the LLM to generate fixed code, displays a diff, and saves changes only when the user accepts them.

## Requirements coverage

| Required feature | Implementation | Status |
| --- | --- | --- |
| Read an existing Python file and request bug detection, PEP 8 review, and refactoring suggestions | [main.py](main.py) reads the bundled `python-files/incorrect_sample.py` and sends its source to `gpt-4o` with a structured review prompt. | Complete |
| Parse the response into a structured report with issue, line, and suggestion fields | Pydantic `Issue` and `Response` models define the report, including the original snippet and approximate-line flag. | Complete |
| Validate required fields and reject entries with invalid or empty values | Pydantic validates required fields and their types. `validateResponse()` rejects nonpositive line numbers and blank descriptions, suggestions, or source snippets. | Complete |
| Mark line references as approximate when they cannot be verified against the file | `validateLineAndSnippt()` compares the snippet with the original source line, including exact indentation and whitespace. Unverified findings are marked approximate. | Complete |
| Review and report suggestions without automatically executing or applying generated changes | The program lists findings and displays a diff. It writes fixed content to the input file only after the user explicitly accepts the changes, and never executes the reviewed code. | Complete |

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

The CLI lists each issue with its original code snippet, line number, approximate-line flag, and suggestion. All findings remain in the report, including approximate references.

Illustrative output for a one-line file containing `total=0`; generated findings and suggested wording can vary:

```text
1: PEP 8: Missing spaces around the assignment operator.
Code Snippet: total=0
Suggestion: Add spaces around the assignment operator.
Line: 1
-------------------------------------
```

After listing the issues, the CLI generates fixed code, then asks the LLM to produce a readable diff. Enter `y` or `yes` to replace the input file with the fixed content; letter case and surrounding whitespace are ignored. Any other answer leaves the file unchanged. If the fixed content is identical to the original, it prints `No changes to apply.` without requesting a diff, prompting, or writing the file.

### Applying fixes from Python

`applyFixes(content, response)` sends the original source and structured review to the LLM and returns the complete corrected source as a string:

```python
from main import getLLMResponse, applyFixes, generateDiff

response = getLLMResponse(content)
corrected_content = applyFixes(content, response)
print(generateDiff(corrected_content, content))
```

The editing prompt requests minimal, coordinated fixes and preservation of indentation and unchanged formatting. Returned whitespace is preserved without trimming. With no reported issues, the function returns the original content without an API call. The function returns a string; the CLI handles displaying the diff and saving accepted changes.

`generateDiff(new_content, old_content)` sends both versions to the LLM and returns its diff labeled `original` and `fixed`, with removed lines prefixed by `-` and added lines by `+`. The prompt requests exact indentation and a little context around each changed block. Identical content returns an empty string without an API call. Missing or blank model output raises an error before the CLI asks to save changes.

## Demo

Demo not recorded yet for the current version.

**Limitation:** AI suggestions and the generated diff may be incomplete or incorrect. Line verification checks only the source reference; it does not establish that a finding, suggestion, or diff is correct.
