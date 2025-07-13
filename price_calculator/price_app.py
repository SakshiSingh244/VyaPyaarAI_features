import streamlit as st
from scraper.meesho_scraper import scrape_meesho_prices

st.set_page_config(page_title="Online Price Calculator", layout="centered")

st.title("🛒 Online Price Calculator")
st.markdown("Search and compare prices of products across e-commerce platforms (currently supports Meesho).")

# Platform dropdown (only Meesho works for now)
platform = st.selectbox("Select platform", ["Meesho", "Flipkart (coming soon)", "Amazon (coming soon)"])

product_name = st.text_input("Enter product name (e.g., saree, kurti, shoes)")
cost_price = st.number_input("Enter your cost price (₹)", min_value=0, step=1)

if st.button("Calculate Prices and Suggest Selling Price"):
    if not product_name.strip():
        st.warning("Please enter a product name.")
    elif cost_price <= 0:
        st.warning("Please enter a valid cost price greater than 0.")
    elif platform != "Meesho":
        st.info(f"🔧 {platform} support coming soon! Currently only Meesho is supported.")
    else:
        with st.spinner(f"Scraping {platform} for '{product_name}'..."):
            result = scrape_meesho_prices(product_name)

        if "error" in result:
            st.error(f"❌ Error: {result['error']}")
        else:
            st.success("✅ Price data fetched successfully!")
            st.metric("Minimum Price", f"₹{result['min']}")
            st.metric("Maximum Price", f"₹{result['max']}")
            st.metric("Average Price", f"₹{result['avg']}")
            st.markdown(f"🧾 Total items checked: **{result['count']}**")

            # Suggested selling prices
            min_sell = max(cost_price, result['min'])
            recommended_sell = max(cost_price, int(cost_price * 1.2))  # 20% margin
            max_sell = result['max']

            st.markdown("### Suggested Selling Prices 💡")
            st.write(f"- **Minimum competitive price:** ₹{min_sell}")
            st.write(f"- **Recommended price (cost + 20% margin):** ₹{recommended_sell}")
            st.write(f"- **Maximum price (premium):** ₹{max_sell}")
