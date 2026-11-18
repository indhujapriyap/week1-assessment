import os 
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("API_KEY")
print("API KEY LOADED:",api_key is not None)