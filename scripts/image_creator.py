from openai import OpenAI
import os
import requests
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover_image(topic: str) -> str:
    print("🎨 Creating DALL·E image...")

    response = client.images.generate(
        model="dall-e-3",  # or "dall-e-2" if 3 is not available on your account
        prompt=f"Beautiful Etsy-style cover image for a digital product titled '{topic}'",
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url
    os.makedirs("images", exist_ok=True)
    image_path = f"images/{topic.replace(' ', '_')}.png"
    
    image_data = requests.get(image_url).content
    with open(image_path, "wb") as f:
        f.write(image_data)

    return image_path
