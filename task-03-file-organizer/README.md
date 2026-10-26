# Task 3 — Automated File Organizer

**Level:** Level 2

**Status:** Complete

A command-line tool for grouping files into extension-based subfolders while preserving existing destination files. It prompts for a directory and dry-run choice, previews changes without moving files when requested, and records operations and errors in a log file.

## Requirements coverage

| Required feature | Implementation | Status |
| --- | --- | --- |
| Scan a target directory and sort files into subfolders by extension | [directoryToDict](main.py#L22) groups top-level files; [addToSubfolders](main.py#L55) moves them. Answer `N` at the interactive prompt to use normal move mode. | Complete |
| Never overwrite an existing destination file; rename the incoming file on conflict | [Destination checks and renaming](main.py#L75) select names such as `notes.txt(1)`, leaving existing files intact. Verified on Windows through direct function calls and the CLI. | Complete |
| Report each move with filename, source, and destination | [Move summaries](main.py#L86) record all three fields in `log.log`. The file-logging bonus replaces console operation messages; input prompts remain in the console. | Complete |
| Handle duplicate filenames, missing permissions, and empty folders gracefully | [Per-file error handling](main.py#L99) logs and skips files that fail, allowing other files to continue. [Directory error handling](main.py#L6) logs scanning or setup failures and stops the run. | Complete |

## Bonuses and additional features

Official bonus features:

- **File logging — Complete.** Uses Python's `logging` module with `INFO`, `WARNING`, and `ERROR` entries in a UTF-8 log file.
- **Dry-run mode — Complete.** Answer `Y` to log planned folder creation, moves, and conflict renames without creating folders or moving files. Verified with missing, empty, and populated destination folders, including multiple filename conflicts.


## Setup

Python 3 is required; verification used Python 3.14.6. The program uses only Python's standard library: `os`, `sys`, `pathlib`, and `logging`. No virtual environment, dependency installation, API accounts, or environment variables are needed.

From the repository root, enter the task directory:

```sh
cd task-03-file-organizer
```

## Usage

Launch the interactive script:

```sh
python main.py
```

Use `python3 main.py` if your system uses the `python3` command. Enter an **absolute directory path** when prompted.

Answer uppercase `Y` to preview changes or `N` to move files. Only uppercase `Y` enables dry-run; all other answers select normal move mode.

For a disposable example in PowerShell, create a sample directory with different file types, an existing destination file, and an unrelated subfolder:

```powershell
$sampleDirectory = Join-Path $env:TEMP ("elevvo-demo-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path (Join-Path $sampleDirectory ".txt") -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $sampleDirectory "archive.v1") -Force | Out-Null
Set-Content -LiteralPath (Join-Path $sampleDirectory "notes.txt") -Value "incoming sample"
Set-Content -LiteralPath (Join-Path $sampleDirectory ".txt\notes.txt") -Value "existing sample"
Set-Content -LiteralPath (Join-Path $sampleDirectory "data.csv") -Value "name,value"
Set-Content -LiteralPath (Join-Path $sampleDirectory "README") -Value "extensionless sample"
Set-Content -LiteralPath (Join-Path $sampleDirectory "archive.v1\keep.txt") -Value "leave this subfolder unchanged"
$sampleDirectory
python main.py
```

Paste the full path printed by `$sampleDirectory` and answer `Y`. This previews folder creation, moves, and the duplicate-name rename while leaving all sample files and folders unchanged.

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

Run `python main.py` again with the same sample path and answer `N` to apply the moves. The existing `.txt` folder is reused, the incoming duplicate becomes `notes.txt(1)`, and `archive.v1` and its contents stay untouched.

Expected sample layout after normal mode:

```text
elevvo-demo-<id>/
├── .csv/
│   └── data.csv
├── .txt/
│   ├── notes.txt       (existing file preserved)
│   └── notes.txt(1)    (incoming file renamed)
├── Others/
│   └── README
└── archive.v1/
    └── keep.txt        (existing subfolder unchanged)
```

Runtime logs are [ignored by Git](../.gitignore).

## Demo

The demo shows the program running in a chosen directory in both dry-run and normal modes, including duplicate filenames being renamed without overwriting existing files, reuse of existing extension folders, unrelated subfolders remaining unchanged, and the resulting log output.

https://github.com/user-attachments/assets/389521a6-e81c-48fc-8df9-9a1bcd7d1927
