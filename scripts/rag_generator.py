# scripts/rag_generator.py

import os
import openai
from dotenv import load_dotenv
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_rag_text(topic: str, context: str) -> str:
    print("🧠 Generating RAG content...")
    prompt = f"""
You're a top digital product creator on Etsy. Write a clear, engaging 3-page guide on the topic: "{topic}".
Use this background info for inspiration (don't copy directly):
{context}

Organize your guide with sections, bullet points, and practical tips.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content


def save_to_pdf(text: str, topic: str) -> str:
    print("📄 Saving guide as PDF...")
    os.makedirs("docs", exist_ok=True)
    path = f"docs/{topic.replace(' ', '_')}.pdf"
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    flowables = [Paragraph(p.strip(), styles['Normal']) for p in text.split('\n') if p.strip()]
    doc.build(flowables)
    return path

def generate_document(topic: str, context: str) -> str:
    text = generate_rag_text(topic, context)
    return save_to_pdf(text, topic)
