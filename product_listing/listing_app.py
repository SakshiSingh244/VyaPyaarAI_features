# product_listing/listing_app.py

import streamlit as st
from gemini_api import generate_product_listing

st.set_page_config(page_title="📝 Product Listing Generator", layout="centered")

st.title("📦 AI Product Listing Generator")
st.markdown("Generate high-conversion product listings using Gemini AI.")

# Inputs
product_name = st.text_input("Enter Product Name (e.g., Cotton Saree, Leather Wallet)")
product_description = st.text_area("Describe your product (materials, target, use case, etc.)")

if st.button("Generate Listing"):
    if not product_name.strip() or not product_description.strip():
        st.warning("Please provide both product name and description.")
    else:
        with st.spinner("Generating listing using Gemini..."):
            result = generate_product_listing(product_name, product_description)

        if result.startswith("❌"):
            st.error(result)
        else:
            st.success("✅ Listing Generated")
            st.markdown("---")
            st.markdown(result)
