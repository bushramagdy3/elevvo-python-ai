# Task 7 — LLM-Powered Document Q&A Tool

**Level:** Industry Level

**Status:** Planned

Planned tool for answering questions from supplied documents with supporting citations. The current interface is a command-line placeholder that reports the project is planned; application behaviour has not been implemented.

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
cd task-07-document-qa
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux:

```sh
cd task-07-document-qa
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
Task 7 — LLM-Powered Document Q&A Tool is planned. Implementation is not available yet.
```

The placeholder exits with status 1 to indicate that the application is unavailable. It accepts no input; a complete application interaction will be documented after implementation.

## Demo

Demo not recorded yet

Recording checklist for a roughly 60–90 second demo after implementation:

- Answer a question from sample documents and cite the supporting chunks.
- Decline an unrelated question that falls below the configured retrieval threshold.
- Include an implemented bonus if available, using safe sample data without credentials.

## Tests and evaluation

No project tests or test command are available yet. No project test results are claimed. Add tests under `tests/` when implementation begins; the usage command above only invokes the placeholder.

Planned checks from the [repository guide](../README_GUIDE.md):

- A supported question produces an answer with relevant supporting chunks.
- An unrelated question below the retrieval threshold is declined.
- Document-loading failures and model/API errors are handled clearly.

Planned evaluation cases; these are targets, not observed results. Neither mocked model/API tests nor live integration checks have been run.

| Input | Expected behaviour | Observed result | Pass/fail |
| --- | --- | --- | --- |
| Question supported by a supplied document | Answer with supporting chunk citations | Not evaluated | Not run |
| Question unrelated to the supplied documents | Decline when the retrieval score is below the configured threshold | Not evaluated | Not run |
| Unreadable document or unavailable model/API | Provide a clear failure response | Not evaluated | Not run |

## Design decisions and limitations

Document loading, chunking, retrieval, and answer generation are not implemented. Supported formats, the scoring method, and the retrieval threshold remain unset and must be documented with their actual values once implemented. Model choice, download requirements, network access, costs, and evaluation limits are also undecided; model answers will require verification.
