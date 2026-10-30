# Task 7 — LLM-Powered Document Q&A Tool

**Level:** Industry Level

**Status:** Complete

A retrieval-augmented generation (RAG) tool for answering questions about five short sample recipe documents. It creates local embeddings, retrieves relevant chunks from a Chroma vector store, and generates an answer with source filenames and full supporting chunks. The application offers a command-line interface and a Gradio web interface, with a configurable distance threshold and a code-enforced refusal when no relevant chunks qualify.

## Requirements coverage

| Required feature | Implementation | Status |
| --- | --- | --- |
| Build a minimal RAG tool using 3–5 short sample text documents | Five sample recipes are included in [recipe_documents](recipe_documents/). | Complete |
| Split documents into chunks, generate embeddings, and store them in a basic vector store | [prepare-documents.py](prepare-documents.py) uses a 500-character chunk limit with 100-character overlap, the `all-mpnet-base-v2` SentenceTransformer model, and a persistent Chroma collection named `recipes`. | Complete |
| Retrieve similar chunks, pass them to an LLM, and cite the chunks used | [main.py](main.py) retrieves the top three candidates, filters them by distance, and sends accepted chunks to `gpt-4o`. Structured responses include the answer and citations with a source filename and the full supporting chunk. | Complete |
| Define a clear, configurable threshold and decline unsupported questions without relying only on prompt wording | `MAX_DISTANCE = 1.0` controls accepted retrieval distances. If no chunk qualifies, `getResponse()` returns `I don't know. Ask something else.` with no citations before calling the LLM. | Complete |
| Check questions with no relevant answer in the document set | The refusal path is exercised with an unsupported question and no qualifying contexts; the application returns its fixed refusal without an LLM call. | Complete |
| Use sample or public documents | The indexed input consists of the five supplied sample recipe text files. Embeddings are generated locally; the question and retrieved sample chunks are sent to the OpenAI API for answer generation. | Complete |

## Bonuses and additional features

**Official bonus — Simple web interface: Complete.** [app.py](app.py) provides a Gradio interface with a `Query` input and separate `Response` and `Citations` outputs. Citations display numbered source filenames and their supporting chunks.

Additional features:

- Repeated questions in the CLI until the user enters `Exit`.
- Structured answers and citations defined with Pydantic models.
- A persistent local index that can be reused across application launches.

## Setup

Use Python 3.14. Local verification used Python 3.14.6. An OpenAI API key and access to the configured `gpt-4o` model are required. The embedding model downloads on first use and is cached locally; OpenAI requests require internet access and are subject to account limits and usage charges.

Run the following from the repository root.

Windows PowerShell:

```powershell
cd task-07-document-qa
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```sh
cd task-07-document-qa
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
| `OPENAI_API_KEY` | Authenticates answer-generation requests to the OpenAI API. |

The application reads this file with `python-dotenv`. Start the scripts from `task-07-document-qa` so the configuration and relative data paths resolve correctly. Local `.env` files and the generated `vectorDB` directory are excluded from version control.

### Prepare the document index

Before launching either interface in a fresh checkout, run:

```sh
python prepare-documents.py
```

This reads the sample recipes, splits their text into chunks, generates embeddings on the CPU, and stores the chunks, vectors, and source filenames in the `recipes` collection under `vectorDB/`.

Prepare the index once and reuse it for subsequent launches. Changes to documents, chunking, or the embedding model require rebuilding the index; rerunning preparation uses the same record IDs and collection.

### Configure retrieval

Edit the setting near the top of [main.py](main.py):

```python
MAX_DISTANCE = 1.0
```

The application retains candidates whose Chroma distance is less than or equal to this value. Smaller distances indicate closer matches. Lowering the cutoff makes retrieval stricter; increasing it admits more candidates. The collection uses Chroma's default squared L2 distance, so this value is a distance cutoff rather than a percentage confidence score.

## Usage

### Gradio web interface

From the task directory with the virtual environment active:

```sh
python app.py
```

Open the local URL printed in the terminal. Enter a question in `Query` and submit it. The `Response` field displays the answer, while `Citations` displays the source filenames and full supporting chunks.

Example question:

```text
How many servings does the tomato and basil pasta recipe make?
```

When no chunks meet the configured threshold, the response is `I don't know. Ask something else.` and the citations output is empty. Stop the local server with `Ctrl+C` in the terminal.

### Command-line interface

```sh
python main.py
```

Ask questions at the prompt. Enter `Exit`, ignoring case and surrounding whitespace, to end the session.

Illustrative complete interaction; generated wording and retrieved chunks can vary. The unrelated-question example assumes no retrieved chunk passes the distance cutoff:

```text
Welcome, ask anything: How many servings does the tomato and basil pasta recipe make?
Response : The tomato and basil pasta recipe serves 2.
Citation : 01_tomato_basil_pasta.txt
RECIPE: Tomato and Basil Pasta Recipe ID: R01 Servings: 2 Preparation time: 10 minutes Cooking time: 20 minutes Equipment: Large saucepan, frying pan, colander  OVERVIEW Tomato and basil pasta combines spaghetti with a simple tomato sauce. This version uses no cream, butter, or cheese. Use dried wheat spaghetti and serve the dish immediately after mixing it with the sauce.
Enter 'Exit' to exit the program
Ask anything: What is the capital of Australia?
Response : I don't know. Ask something else.
Enter 'Exit' to exit the program
Ask anything: Exit
```

## Demo

The recording demonstrates the project running in both the command-line and Gradio web interfaces. Each interface is used to ask questions relevant to the recipe documents and unrelated questions, showing answers with source filenames and full supporting chunks for relevant questions, and the refusal message for unrelated questions.

`TASK_7_DEMO_URL`
