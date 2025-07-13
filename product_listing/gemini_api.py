# product_listing/gemini_api.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ Gemini API key not found in .env file!")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')
print(f"Loaded API key: {repr(api_key)}")

def generate_product_listing(product_name, product_description):
    prompt = f"""
You are a professional e-commerce copywriter. Create a compelling product listing for the following item:

**Product Name**: {product_name}

**Product Description**: {product_description}

Your output should include:
- A catchy title
- 3-5 bullet points of features/benefits
- A short, SEO-optimized description
- Use persuasive language suitable for Meesho or Flipkart audience.
- Keep the tone friendly and trust-building.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating content: {e}"
