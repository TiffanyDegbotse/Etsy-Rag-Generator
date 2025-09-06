# main.py

from scripts.topic_scraper import scrape_context
from scripts.rag_generator import generate_document
from scripts.image_creator import generate_cover_image
from scripts.etsy_listing_helper import generate_listing_text

def main():
    print("💡 Etsy AI Product Generator")
    topic = input("Enter your digital product topic (e.g. Self-Care Journal): ").strip()

    context = scrape_context(topic)
    pdf_path = generate_document(topic, context)
    image_path = generate_cover_image(topic)
    listing_text = generate_listing_text(topic)

    print("\n✅ All Done!")
    print(f"📄 PDF: {pdf_path}")
    print(f"🖼️ Image: {image_path}")
    print("\n🛍️ Etsy Listing:\n")
    print(listing_text)

if __name__ == "__main__":
    main()
