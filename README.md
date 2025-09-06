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
etsy-ai-generator/
├── data/
├── docs/
├── images/
├── scripts/
│   ├── topic_scraper.py
│   ├── rag_generator.py
│   ├── image_creator.py
│   └── etsy_listing_helper.py
├── main.py
├── .env.example
└── requirements.txt

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

