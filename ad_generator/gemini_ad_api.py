# ad_generator/gemini_ad_api.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ Gemini API key not found in .env")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_ad_content(product, description):
    prompt = f"""
You are a creative ad copywriter.

Generate marketing content for the following product:

**Product**: {product}
**Description**: {description}

Output format:
1. A catchy ad headline
2. 1-2 paragraph persuasive ad copy (for Meesho, Flipkart, etc.)
3. 2-3 catchy one-liners or taglines for social media use

Keep it engaging, trust-building, and suitable for Indian online buyers.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating content: {e}"
