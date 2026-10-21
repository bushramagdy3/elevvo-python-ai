# Task 3 — Automated File Organizer

**Level:** Level 2

**Status:** Planned

Planned tool for organizing files into folders by extension. The current interface is a command-line placeholder that reports the project is planned; application behaviour has not been implemented.

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
cd task-03-file-organizer
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux:

```sh
cd task-03-file-organizer
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
Task 3 — Automated File Organizer is planned. Implementation is not available yet.
```

The placeholder exits with status 1 to indicate that the application is unavailable. It accepts no input; a complete application interaction will be documented after implementation.

## Demo

Demo not recorded yet

Recording checklist for a roughly 60–90 second demo after implementation:

- Sort a disposable sample folder by extension.
- Show an incoming filename conflict and confirm both files remain intact.
- Include an implemented bonus if available, using safe sample data without credentials.

## Tests and evaluation

No project tests or test command are available yet. No project test results are claimed. Add tests under `tests/` when implementation begins; the usage command above only invokes the placeholder.

Planned checks from the [repository guide](../README_GUIDE.md):

- Files with different extensions are placed in the intended folders.
- Conflicting destination filenames preserve both files.
- Missing or invalid source paths receive a clear response.

## Design decisions and limitations

File classification, destination naming, and conflict handling are not implemented. Use disposable copies for future examples and tests; file-moving behaviour must be verified before use on valuable files.
