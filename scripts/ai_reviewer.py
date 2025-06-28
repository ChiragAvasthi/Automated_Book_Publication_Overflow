import os
from dotenv import load_dotenv
load_dotenv()

def review_chapter(text):
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return "[REVIEW MOCK] Looks good. Consider simplifying some sentences."
    return "[REVIEW] This would use OpenAI to review text"
