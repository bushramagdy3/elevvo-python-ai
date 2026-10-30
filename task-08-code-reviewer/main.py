from openai import Client
import dotenv
import os
from pydantic import BaseModel
from pathlib import Path

client = Client(api_key=dotenv.get_key(dotenv_path='.env', key_to_get="OPENAI_API_KEY"))



if __name__ == "__main__":
    # path = input("Write the path of the Python file")
    path = Path(os.getcwd, "python-file", "correct_sample")
    with open(path, "r") as file:
        content = path.read_text()
        