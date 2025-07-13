# test.py
from scraper.meesho_scraper import scrape_meesho_prices

if __name__ == "__main__":
    product = input("Enter product name to search on Meesho: ")
    result = scrape_meesho_prices(product)

    if "error" in result:
        print("Error:", result["error"])
    else:
        print(f"Min Price: ₹{result['min']}")
        print(f"Max Price: ₹{result['max']}")
        print(f"Average Price: ₹{result['avg']}")
        print(f"Total Items Found: {result['count']}")
