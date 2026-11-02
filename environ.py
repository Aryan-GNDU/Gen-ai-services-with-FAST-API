import os

import dotenv

dotenv.load_dotenv()

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment variables.")
else:
    print("API_KEY is set successfully.")