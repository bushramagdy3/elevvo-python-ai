"""Implementation placeholder for Task 7: LLM-Powered Document Q&A Tool."""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
import os

DOCS_PATH = Path(os.getcwd(),"recipe_documents")

def getDocumentsChunks(path :str = DOCS_PATH):
    os.chdir(path)

    chunks = list()

    splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,       
                chunk_overlap=100,     
                length_function=len    
            )

    for doc in os.listdir():
        with open(Path(os.getcwd(),doc), "r") as file:
            content = file.read()

        chunks.extend(chunk.replace('\n', " ") for chunk in splitter.split_text(content))

    return chunks

if __name__ == "__main__":
    print(getDocumentsChunks())
