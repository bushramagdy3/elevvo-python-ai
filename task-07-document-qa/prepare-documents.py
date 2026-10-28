from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
import os
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
import logging

DOCS_PATH = Path(os.getcwd(),"recipe_documents")
embedding_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", device="cpu")
client = PersistentClient(path=os.chdir())
collection = client.get_or_create_collection(name = "recipes")

def getDocumentsChunks(path :str = DOCS_PATH):
    logging.info("Getting chunks...")

    os.chdir(path)

    chunks = list()

    splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,       
                chunk_overlap=100,     
                length_function=len    
            )

    for doc in os.listdir():
        logging.info(f"Chunking {doc}...")
        with open(Path(os.getcwd(),doc), "r") as file:
            content = file.read()

        chunks.extend({"source": doc, "chunk": chunk.replace('\n', " ")} for chunk in splitter.split_text(content))

    return chunks

def embedChunks(chunks :list[dict]):
    logging.info("Embedding chunks...")
    for chunk in chunks:
        chunk["embedding"] = embedding_model.encode(chunk["chunk"])
    return chunks

def saveEmbeddingToVectorStore(embeddings :list, chunks :list):
    logging.info("Storing chunks to chromaDB collection")
    embeddings = [chunk["embedding"] for chunk in chunks]
    collection.add(
        ids = range(0, len(chunks) - 1),
        documents = chunks,
        embeddings = embeddings,
        metadatas = [{"source": chunk["source"]} for chunk in chunks]
    )

def prepareDocuments(path :str = DOCS_PATH):
    chunks = getDocumentsChunks(path)
    embeddings = embedChunks(chunks)
    saveEmbeddingToVectorStore(embeddings, chunks)

if __name__ == "__main__":
    logging.basicConfig(level=logging.info)
    logging.info("Peparing documents...")
    prepareDocuments()
