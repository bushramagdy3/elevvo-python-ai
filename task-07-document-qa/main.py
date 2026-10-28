from sentence_transformers import SentenceTransformer
from openai import OpenAI
import dotenv

OPENAI_API_KEY = dotenv.get_key(key_to_get="OPENAI_API_KEY", dotenv_path=".env")
embedding_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", device="cpu")
client = OpenAI(api_key=OPENAI_API_KEY)


def embedQuery(query :str):
    return embedding_model.encode(query)

def semanticSearch(embeddedQuery :str):
    pass

def callLLM(query :str,  context :str):
    pass

if __name__ == "__main__":
    pass
