from ddgs import DDGS  # if you're using the renamed version
import os

def scrape_context(topic: str, max_results=5) -> str:
    print(f"🔍 Scraping DuckDuckGo for topic: {topic}")
    context = []
    with DDGS() as ddgs:
        for r in ddgs.text(topic, max_results=max_results):
            if 'body' in r:
                context.append(r['body'])
    output = "\n".join(context)
    
    os.makedirs("data", exist_ok=True)
    with open(f"data/{topic.replace(' ', '_')}_context.txt", "w", encoding="utf-8") as f:
        f.write(output)

    return output
