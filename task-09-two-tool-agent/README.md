# Task 9 — AI Agent for a Two-Tool Task

**Level:** Industry Level

**Status:** Planned

Planned AI agent for completing a goal using two configured tools. The current interface is a command-line placeholder that reports the project is planned; application behaviour has not been implemented.

## Requirements coverage

The official task PDF is not included in this repository. The requirements mapping needs verification against that document before implementation or completion claims can be made.

| Required feature | Implementation | Status |
| --- | --- | --- |
| Official task requirements — mapping needs verification | No project implementation; [main.py](main.py) only reports the planning status. | Not implemented |

## Bonuses and additional features

Official bonuses have not been verified because the task PDF is unavailable; none are implemented. No additional features are implemented.

The optional third-tool mode mentioned in the [repository guide](../README_GUIDE.md) is not implemented.

## Setup

A working Python 3 installation is needed to run the placeholder. No Python version has been tested for this project yet. Run the following from the repository root.

Windows PowerShell:

```powershell
cd task-09-two-tool-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux:

```sh
cd task-09-two-tool-agent
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
Task 9 — AI Agent for a Two-Tool Task is planned. Implementation is not available yet.
```

The placeholder exits with status 1 to indicate that the application is unavailable. It accepts no input; a complete application interaction will be documented after implementation.

## Demo

Demo not recorded yet

Recording checklist for a roughly 60–90 second demo after implementation:

- Complete a goal using both configured tools and show their input/output logs.
- Show a handled tool failure and demonstrate the execution limit stopping an unfinished run.
- Include an implemented bonus if available, using safe sample data without credentials.

## Tests and evaluation

No project tests or test command are available yet. No project test results are claimed. Add tests under `tests/` when implementation begins; the usage command above only invokes the placeholder.

Planned checks from the [repository guide](../README_GUIDE.md):

- A suitable goal completes using the two configured tools.
- A tool failure is handled and recorded clearly.
- The execution limit stops an unfinished run.
- Logs contain tool inputs and outputs without hidden model reasoning.

Planned evaluation cases; these are targets, not observed results. Neither mocked model/API tests nor live integration checks have been run.

| Input | Expected behaviour | Observed result | Pass/fail |
| --- | --- | --- | --- |
| Goal requiring both configured tools | Complete the goal and log tool inputs and outputs | Not evaluated | Not run |
| A configured tool returns an error | Handle and log the tool failure | Not evaluated | Not run |
| Goal remains unfinished at the execution limit | Stop execution at the configured limit | Not evaluated | Not run |

## Design decisions and limitations

The two tools, model, and execution limit have not been selected. Tool execution, failure handling, and input/output logging are not implemented. The default mode is planned to use two tools; any optional third-tool mode must be documented separately if implemented. Network dependencies, credentials, costs, and tool side effects depend on the eventual choices.
