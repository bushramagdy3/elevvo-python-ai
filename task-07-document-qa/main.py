"""Implementation placeholder for Task 7: LLM-Powered Document Q&A Tool."""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
import os
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import dotenv

DOCS_PATH = Path(os.getcwd(),"recipe_documents")
OPENAI_API_KEY = dotenv.get_key(key_to_get="OPENAI_API_KEY", dotenv_path=".env")
embedding_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", device="cpu")
client = OpenAI(api_key=OPENAI_API_KEY)


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

def embedChunks(chunks :list[str]):
    return embedding_model.encode(chunks)

def saveEmbeddingToVectorStore(embeddings :list):
    pass

def embedQuery(query :str):
    return embedding_model.encode(query)

def semanticSearch(embeddedQuery :str):
    pass

def callLLM(query :str,  context :str):
    pass

if __name__ == "__main__":
    chunks = getDocumentsChunks()
    embeddings = embedChunks(chunks)
    print(embeddings)
