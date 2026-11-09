# Task 8 — AI-Assisted Code Review Tool

**Level:** Industry Level

**Status:** Complete

A command-line tool that reviews an existing Python file using the OpenAI API. It produces structured findings for bugs, PEP 8 compliance, and refactoring, validates the report, and marks unverified line references as approximate. The CLI lists issues and suggestions, asks the LLM to generate fixed code, runs another LLM pass for naming consistency and code quality, displays a diff, and saves changes only when the user accepts them.

## Requirements coverage

The official task PDF is not included in this repository. The table describes implemented behavior; its mapping to the official requirements needs verification against that document.

| Required feature | Implementation | Status |
| --- | --- | --- |
| Read an existing Python file and request bug detection, PEP 8 review, and refactoring suggestions | [main.py](main.py) reads the bundled `python-files/incorrect_sample.py` and sends its source to `gpt-4o` with a structured review prompt. | Complete |
| Parse the response into a structured report with issue, line, and suggestion fields | Pydantic `Issue` and `Response` models define the report, including the original snippet and approximate-line flag. | Complete |
| Validate required fields and reject entries with invalid or empty values | Pydantic validates required fields and their types. `validateResponse()` rejects nonpositive line numbers and blank descriptions, suggestions, or source snippets. | Complete |
| Mark line references as approximate when they cannot be verified against the file | `validateLineAndSnippt()` compares the snippet with the original source line, including exact indentation and whitespace. Unverified findings are marked approximate. | Complete |
| Review and report suggestions without automatically executing or applying generated changes | The program lists findings and displays a diff. It writes fixed content to the input file only after the user explicitly accepts the changes, and never executes the reviewed code. | Complete |

## Bonuses and additional features

- **Before/after diff with manual acceptance or rejection:** Displays the exact text changes using Python's `difflib.unified_diff` and asks before overwriting the source file.
- **LLM-generated fixes:** Applies the review suggestions to the complete source, including coordinated changes across multiple lines.
- **Naming and quality refinement:** Runs another LLM pass to resolve partial renames, check PEP 8 naming and formatting, and make small refactors.
- **Whitespace handling:** Preserves returned indentation, normalizes line endings for comparison, marks missing final newlines, and uses the original file's detected line-ending style when saving.

These additions are implemented. Their classification as official bonuses needs verification against the task PDF.

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

The application reads this file with `python-dotenv`. Start the script from `task-08-code-reviewer` so the configuration file is found. Local `.env` files are excluded from version control. The source, review report, and proposed fixes are sent to the OpenAI API during the relevant processing steps.

## Usage

From the task directory with the virtual environment active:

```sh
python main.py
```

The script reviews `python-files/incorrect_sample.py` by default. To review another file, change the `path` assignment in the `__main__` block of [main.py](main.py).

[python-files/incorrect_sample.py](python-files/incorrect_sample.py) contains deliberate bugs and style issues. [python-files/correct_sample.py](python-files/correct_sample.py) provides a working example, including explicit handling of empty input.

The program:

1. Reads the file as UTF-8 and requests a structured review.
2. Lists validated issues with their source snippets, line numbers, approximate-reference labels, and suggestions. A snippet must match its source line exactly, including indentation, to receive a verified reference.
3. Sends the source and report to `applyFixes()` to generate corrected code.
4. Sends that code to `refineFixedCode()` for another check of names, references, style, and remaining bugs.
5. Compares the final code with the original using a local Python diff.
6. Asks whether to save the final code to the same file.

Illustrative interaction after setting `path` to a one-line file containing `total=0`; generated findings and fixes can vary:

```text
1: PEP 8: Missing spaces around the assignment operator.
Code Snippet: total=0
Suggestion: Add spaces around the assignment operator.
Line: 1
-------------------------------------
Proposed changes:
--- original
+++ fixed
@@ -1 +1 @@
-total=0
+total = 0

Accept these changes and save the file? (Y/N) N
Changes rejected. File unchanged.
```

Enter `y` or `yes` to replace the input file with the final refined content; letter case and surrounding whitespace are ignored. Any other answer leaves the file unchanged. When saving succeeds, the CLI prints `Changes saved to <path>.` If the final content has no differences other than line-ending style, it prints `No changes to apply.` without prompting or writing the file. The reviewed code is never executed by the tool.

### Applying fixes from Python

`applyFixes(content, response)` sends the original source and structured review to the LLM and returns the complete corrected source as a string:

```python
from main import getLLMResponse, applyFixes, refineFixedCode, generateDiff

response = getLLMResponse(content)
corrected_content = applyFixes(content, response)
corrected_content = refineFixedCode(corrected_content)
print(generateDiff(corrected_content, content))
```

The editing prompt requests minimal, coordinated fixes and preservation of indentation and unchanged formatting. Returned whitespace is preserved without trimming. With no reported issues, the function returns the original content without an API call. The function returns a string; the CLI handles displaying the diff and saving accepted changes.

`refineFixedCode(fixed_content)` runs a separate LLM check for partially renamed functions and variables, scope-aware references, PEP 8 naming and formatting, remaining bugs, and small clarity improvements. It returns the complete refined code, which is used for both the diff and the accepted file contents. This pass also runs when the initial review reports no issues, so it can catch missed inconsistencies. Empty or whitespace-only input is returned without an API call; missing or blank model output for nonblank input raises an error before diff generation or saving.

`generateDiff(new_content, old_content)` uses Python's built-in `difflib.unified_diff` to return a diff labeled `original` and `fixed`, with removed lines prefixed by `-`, added lines by `+`, and context around changed blocks. Line endings are normalized for comparison so Windows CRLF versus Unix LF does not mark unchanged lines as replacements. Indentation is preserved, missing final newlines are marked, and content with no other differences returns an empty string. The CLI saves accepted fixes using the original file's line-ending style. Generating the diff requires no API call.

## Demo

The recording demonstrates reviewing the supplied sample file, displaying structured findings, inspecting the before/after diff and proposed code, rejecting changes with `N`, and accepting changes with `Y`.

`DEMO_VIDEO_URL_HERE`
