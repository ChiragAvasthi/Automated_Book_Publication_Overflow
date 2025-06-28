import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def spin_chapter(text):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "[SPUN MOCK] " + text[::-1]

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a skilled writer. Rewrite the input text to be more engaging and clear, without changing its meaning."},
                {"role": "user", "content": text}
            ],
            temperature=0.7,
            max_tokens=2048
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[SPUN ERROR] {str(e)}"
