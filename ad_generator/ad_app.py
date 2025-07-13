# ad_generator/ad_app.py

import streamlit as st
from gemini_ad_api import generate_ad_content

st.set_page_config(page_title="📢 Ad Content Generator", layout="centered")
st.title("📢 AI-Powered Ad Generator")
st.markdown("Create product ads and taglines using Gemini AI.")

# Input fields
product_name = st.text_input("Enter Product Name")
product_desc = st.text_area("Describe your product in detail")

if st.button("Generate Ad Content"):
    if not product_name.strip() or not product_desc.strip():
        st.warning("Please enter both product name and description.")
    else:
        with st.spinner("Generating ad content..."):
            result = generate_ad_content(product_name, product_desc)

        if result.startswith("❌"):
            st.error(result)
        else:
            st.success("✅ Ad content generated!")
            st.markdown("---")
            st.markdown(result)
