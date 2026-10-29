from sentence_transformers import SentenceTransformer
from openai import OpenAI
import dotenv
from chromadb import PersistentClient
import os
from pathlib import Path
import logging
from pydantic import BaseModel

class Response(BaseModel):
    response : str
    citation : list[Citation]

class Citation(BaseModel):
    chunk :str
    source :str

logging.basicConfig(level=logging.INFO)
logging.info("Initializing app...")

OPENAI_API_KEY = dotenv.get_key(key_to_get="OPENAI_API_KEY", dotenv_path=".env")
embedding_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", device="cpu")
llm = OpenAI(api_key=OPENAI_API_KEY)
client = PersistentClient(path=Path(os.getcwd(), "vectorDB"))
collection = client.get_collection(name="recipes")

def embedQuery(query :str):
    return embedding_model.encode(query)

def getContext(embeddedQuery :str):
    results = collection.query(query_embeddings=[embeddedQuery], n_results=3)
    return [{"document" : results["documents"][0][i] , "source" : results["metadatas"][0][i]["source"]} for i in range(3)]

def callLLM(query :str,  contexts :list[dict]):
    prompt = f"""
        You are a friendly assistant. Answer the user's query based only on contexts, don't answer anything not in the contexts. Return your response along with citation(s). Return a dict with the keys: response, citation. inside citation the keys are: chunk, and source.

        query = {query}

        context = {contexts}
    """
    response = llm.chat.completions.parse(
        model="gpt-4o", 
        messages=[{"role": "system", "content":prompt}, {"role": "user", "content":query}],
        response_format=Response
    ).choices[0].message.parsed

    return response


def getResponse(query :str):
    embeddedQuery = embedQuery(query)
    contexts = getContext(embeddedQuery)
    response = callLLM(query, contexts)
    return response
    

if __name__ == "__main__":

    query = input("Welcome, ask anything: ")

    response = getResponse(query)

    print(f"Response : {response.response}")
    for citation in response.citation:
        print(f"Citation : {citation.source}")
        print(citation.chunk)

