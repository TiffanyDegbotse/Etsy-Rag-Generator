# Etsy RAG Generator 🧠🛍️
This is a CLI tool that uses Retrieval-Augmented Generation (RAG) + DALL·E to:
- ✅ Create digital PDF guides based on trending Etsy topics  
- 🖼️ Generate Etsy-style cover images  
- 🛒 Auto-generate Etsy listing titles, tags, and descriptions  

Features:
- Built with Python + OpenAI API  
- Uses DuckDuckGo Search for RAG context  
- Outputs: PDF guide, 1024x1024 PNG, Etsy-ready listing text  

Usage:
python main.py

Project Structure:

- etsy-ai-generator/
  - data/                       (Scraped RAG context text files)
  - docs/                       (Generated PDF product guides)
  - images/                     (DALL·E-generated Etsy cover images)
  - scripts/
    - topic_scraper.py          (Scrapes topic context from DuckDuckGo)
    - rag_generator.py          (Uses OpenAI to generate the guide and PDF)
    - image_creator.py          (Generates a 1024x1024 cover image via DALL·E)
    - etsy_listing_helper.py    (Creates title, tags, and description for Etsy)
  - main.py                     (Main CLI entry point for full pipeline)
  - requirements.txt            (Python dependencies)
  - .env.example                (Sample environment config)
  - .gitignore                  (Excludes venv, .env, cache, etc.)

Setup:
Create a `.env` file:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx

Install dependencies:
pip install -r requirements.txt

Coming Soon:
- Batch topic generation  
- Etsy auto-upload (via Puppeteer or API)  

Git Commit + Push Example:
git add README.md  
git commit -m "Add README"  
git push
