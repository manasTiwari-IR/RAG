from llama_index.llms.gemini import Gemini
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=gemini_api_key)

def load_model():
    gemini_model = Gemini(model_name="models/gemini-2.5-flash")
    return gemini_model