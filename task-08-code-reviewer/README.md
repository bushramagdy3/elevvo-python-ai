# Task 8 — AI-Assisted Code Review Tool

**Level:** Industry Level

**Status:** Planned

Planned tool for producing structured AI-assisted reviews of supplied code. The current interface is a command-line placeholder that reports the project is planned; application behaviour has not been implemented.

## Requirements coverage

The official task PDF is not included in this repository. The requirements mapping needs verification against that document before implementation or completion claims can be made.

| Required feature | Implementation | Status |
| --- | --- | --- |
| Official task requirements — mapping needs verification | No project implementation; [main.py](main.py) only reports the planning status. | Not implemented |

## Bonuses and additional features

Official bonuses have not been verified because the task PDF is unavailable; none are implemented. No additional features are implemented.

## Setup

A working Python 3 installation is needed to run the placeholder. No Python version has been tested for this project yet. Run the following from the repository root.

Windows PowerShell:

```powershell
cd task-08-code-reviewer
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux:

```sh
cd task-08-code-reviewer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

[requirements.txt](requirements.txt) contains comments only and installs no project dependencies. Application configuration, environment variable names, and external services have not been selected. Add a `.env.example` with placeholders when environment variables are introduced.

## Usage

From the task directory with the virtual environment active:

```sh
python main.py
```

Expected placeholder output:

```text
Task 8 — AI-Assisted Code Review Tool is planned. Implementation is not available yet.
```

The placeholder exits with status 1 to indicate that the application is unavailable. It accepts no input; a complete application interaction will be documented after implementation.

## Demo

Demo not recorded yet

Recording checklist for a roughly 60–90 second demo after implementation:

- Produce a structured review of a deliberately buggy sample file.
- Show a clear response when the input file is missing.
- Include an implemented bonus if available, using safe sample data without credentials.

## Tests and evaluation

No project tests or test command are available yet. No project test results are claimed. Add tests under `tests/` when implementation begins; the usage command above only invokes the placeholder.

Planned checks from the [repository guide](../README_GUIDE.md):

- A deliberately buggy sample receives a structured review.
- A missing input file receives a clear response.
- Malformed model output is rejected or handled by report validation.

Planned evaluation cases; these are targets, not observed results. Neither mocked model/API tests nor live integration checks have been run.

| Input | Expected behaviour | Observed result | Pass/fail |
| --- | --- | --- | --- |
| Deliberately buggy sample code | Produce a structured review with approximate line references | Not evaluated | Not run |
| Missing input file | Provide a clear failure response | Not evaluated | Not run |
| Malformed model response | Handle invalid output through report validation | Not evaluated | Not run |

## Design decisions and limitations

Input handling, model integration, report validation, and approximate line references are not implemented. Supported languages, model choice, network requirements, costs, and input limits remain undecided. The intended review workflow will present suggestions for human review without automatically executing or applying them.
