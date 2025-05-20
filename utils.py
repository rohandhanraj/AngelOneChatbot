import os
from ai_tech_crawler import SmartScraperAgent
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def crawl_angelone_support(base_url="https://www.angelone.in/support"):
    smart_scraper_agent = SmartScraperAgent(
        prompt='',
        source=base_url,
        config={
            "llm": {
                "api_key": os.getenv('OPENAI_API_KEY'),
                "model": "openai/gpt-4o-mini",
            },
        },
        schema={}
    )

    return smart_scraper_agent.load_indepth_and_split(depth=2)