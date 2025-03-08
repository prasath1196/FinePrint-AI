from firecrawl import FirecrawlApp
from dotenv import load_dotenv
from openai import OpenAI
import os
import json
load_dotenv()

def extract_data(url):
    content = scrape_content(url)
    openai_client = OpenAI(api_key=os.getenv('OPEN_AI_KEY'))
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": get_extraction_prompt(content)}],
        response_format={"type": "json_object"},
        temperature=0.2
    )
  
    json_data = json.loads(completion.choices[0].message.content)
    return json_data


def scrape_content(url):
    app = FirecrawlApp(api_key=os.getenv('FIRECRWAL_KEY'))
    scrape_result = app.scrape_url(url, 
        params={
        'formats': ['markdown', 'html'], 
        'mobile': True
        }
    )
    scrape_content = scrape_result['markdown']
    return scrape_content

def get_extraction_prompt(content):
    prompt =f"""
    You are an AI that extracts important information from Terms of Service agreements.  
    Analyze the following document and identify:  

    1. **Hidden fees & auto-renewals**  
    2. **Data privacy (what is collected & who it’s shared with)**  
    3. **Content ownership (does the company own user content?)**  
    4. **Account bans (can users lose access for any reason?)**  
    5. **Legal disputes (does the user waive their right to sue?)**  
    Return the results in **structured JSON** format.  
    ---
    TEXT:
    {content}
    SAMPLE JSON RESPONSE:
    ```json
    "company": "Spotify",
    "hidden_fees": "Auto-renews at $9.99/month after trial. Must cancel manually before renewal.",
    "data_privacy": "Collects browsing history & location. Shares with advertisers.",
    "content_ownership": "Spotify has rights to reuse any uploaded content.",
    "account_bans": "Spotify can suspend accounts permanently for any violation.",
    "legal_disputes": "Users waive right to sue. All disputes go to arbitration."
    ```     
     """   

    return prompt

