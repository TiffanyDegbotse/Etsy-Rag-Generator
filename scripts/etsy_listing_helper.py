# scripts/etsy_listing_helper.py

import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_listing_text(topic: str) -> str:
    print("🛒 Generating Etsy listing content...")

    prompt = f"""
You're an Etsy SEO expert. Create an Etsy product listing for a digital product titled "{topic}".
Return:
1. An optimized Title
2. A persuasive, clear Description (with bullet points)
3. 13 SEO-relevant Tags
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return response.choices[0].message.content
