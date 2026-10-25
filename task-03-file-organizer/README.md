# Task 3 — Automated File Organizer

**Level:** Level 2

**Status:** Complete (core requirements)

A Windows command-line tool for grouping files into extension-based subfolders while preserving existing destination files. It prompts for a directory and dry-run choice, and records operations and errors in a log file; the optional dry-run bonus remains partially implemented.

## Requirements coverage

This mapping follows the supplied Task 3 brief image. The original task PDF is not stored in this repository; the mapping should be cross-checked against that PDF when available.

| Required feature | Implementation | Status |
| --- | --- | --- |
| Scan a target directory and sort files into subfolders by extension | [directoryToDict](main.py#L22) groups top-level files; [addToSubfolders](main.py#L55) moves them. Answer `N` at the interactive prompt to use normal move mode. | Complete |
| Never overwrite an existing destination file; rename the incoming file on conflict | [Destination checks and renaming](main.py#L69) select names such as `notes.txt(1)`, leaving existing files intact. Verified on Windows in direct move-mode checks. | Complete |
| Report each move with filename, source, and destination | [Move summaries](main.py#L79) record all three fields in `log.log`. The file-logging bonus replaces console operation messages; input prompts remain in the console. | Complete |
| Handle duplicate filenames, missing permissions, and empty folders gracefully | [Error handling](main.py#L6) logs failures and stops the run. Direct function checks covered conflicts, empty folders, missing paths, and simulated permission errors. | Complete |

## Bonuses and additional features

Official bonus features:

- **File logging — Complete.** Uses Python's `logging` module with `INFO`, `WARNING`, and `ERROR` entries in a UTF-8 log file.
- **Dry-run mode — Partial.** Answer `Y` to log planned moves and conflict renames without moving files when destination folders already exist. A preview currently stops if a destination folder is missing.

The brief's **Reading ahead** suggestion to schedule runs with cron or Windows Task Scheduler is not implemented.

## Setup

Tested on **Windows with Python 3.14.6**. The program uses only the standard library: `os`, `sys`, `pathlib`, and `logging`. No API accounts, environment variables, or third-party packages are required.

From the repository root, create an optional virtual environment.

Windows PowerShell:

```powershell
cd task-03-file-organizer
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux environment creation:

```sh
cd task-03-file-organizer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The current organizer uses Windows-specific paths; the macOS/Linux commands above create an environment only. Application execution on those platforms is unsupported by the current implementation.

[requirements.txt](requirements.txt) contains comments only, so the installation command installs no packages. Run the application commands below from the task directory.

## Usage

Launch the interactive script:

```powershell
python main.py
```

Enter an **absolute Windows directory path** when prompted.

Answer uppercase `Y` to preview changes or `N` to move files. Only uppercase `Y` enables dry-run; all other answers select normal move mode. Previewing currently requires destination folders to exist already.

For a disposable example, create a sample directory with an existing destination file:

```powershell
$sampleDirectory = Join-Path $env:TEMP ("elevvo-demo-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path (Join-Path $sampleDirectory ".txt") -Force | Out-Null
Set-Content -LiteralPath (Join-Path $sampleDirectory "notes.txt") -Value "incoming sample"
Set-Content -LiteralPath (Join-Path $sampleDirectory ".txt\notes.txt") -Value "existing sample"
$sampleDirectory
python main.py
```

Paste the full path printed by `$sampleDirectory` and answer `Y`. The destination folder is pre-created so this example exercises the working preview case.

Illustrative complete console interaction; the generated path will differ:

```text
Welcome to Bushra's automated file organizer!
Write the path of your targetted directory
C:\Users\Example\AppData\Local\Temp\elevvo-demo-1234
Turn on Dry-run mode? (Y/N)
Y
```

Operations are written to `log.log` beside `main.py`. Each launch overwrites the previous log. From the task directory, inspect it with:

```powershell
Get-Content .\log.log
```

Illustrative log excerpt:

```text
INFO:root:[DRY RUN] Would rename notes.txt to notes.txt(1)
INFO:root:[DRY RUN] Would move file: notes.txt | Source: C:\Users\Example\AppData\Local\Temp\elevvo-demo-1234\notes.txt | Destination: C:\Users\Example\AppData\Local\Temp\elevvo-demo-1234\.txt\notes.txt(1)
INFO:root:File organization run completed successfully.
```

Both sample files remain unchanged during this preview. Run `python main.py` again with the same sample path and answer `N` to move the incoming file to `.txt\notes.txt(1)`, preserving the existing `.txt\notes.txt`. Runtime logs are [ignored by Git](../.gitignore).

## Demo

Demo not recorded yet

Checklist for a roughly 60–90 second recording:

- Organize disposable files with different extensions in normal move mode.
- Demonstrate an existing destination filename and show that both files remain intact.
- Show the working dry-run preview with existing destination folders and its log output, plus a handled invalid-directory error if time permits.

## Tests and evaluation

Verification used Windows, Python 3.14.6, disposable directories, and temporary copies of the script. Permission failures were simulated with `unittest.mock`; real filesystem permission restrictions were not tested.

| Check | Observed result |
| --- | --- |
| 21 direct function checks in normal move mode | Passed: extension grouping, multiple-dot names, exact byte preservation, empty files, spaces, Unicode names, extensionless files, repeated runs, destination-folder reuse, collision handling, summaries, and error handling. |
| CLI preview with existing destination folders | Passed: preview and conflict renames were logged; source and destination contents were unchanged. |
| Answer `N` to select normal mode | Passed: the CLI created the destination folder, moved the sample file, and logged the completed move. |
| Preview with a missing destination folder | Failed: the folder creation was previewed, then entering that uncreated folder stopped the run. |
| Relative target paths | Unsupported in the current implementation; this is a limitation beyond the task's explicit core requirements. |

There is no committed automated test suite or repository test command yet. The 21 function checks were run using a temporary review harness; the interactive cases were run separately on temporary copies of the script.

To repeat the interactive checks, use the disposable sample in [Usage](#usage) and run:

```powershell
python main.py
Get-Content .\log.log
```

Repeat with `N` to verify normal moves. Use a fresh sample directory containing a text file and no `.txt` folder, then answer `Y`, to reproduce the incomplete preview. Inspect the log for errors; handled failures currently can return exit status 0.

## Design decisions and limitations

- Only files directly inside the target directory are processed; subdirectories are skipped.
- Extension grouping is case-insensitive. Folder names retain the suffix's leading dot, such as `.txt` and `.pdf`; extensionless files and names such as `.env` go to `Others`.
- Moves use `Path.rename()` instead of reading and rewriting file contents, preserving bytes and original filename spelling. Conflicts append a number to the whole name, for example `notes.txt(1)`.
- Windows paths and absolute directory inputs are currently required. Helpers change the process's working directory.
- A dry-run preview stops when a required destination folder does not already exist. This affects the optional dry-run bonus, not normal move mode.
- Errors stop the run instead of continuing with other files. Details are recorded in the log; its write mode replaces previous run history.
