import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.farmboy.ca/accessible-store-listing/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    )
}

response = requests.get(URL, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

stores = []

# Get the single wrapper
wrapper = soup.find("div", class_="fb_store_location_wrapper")
if not wrapper:
    raise ValueError("Store wrapper not found")

# Each store is a direct child <div> containing an <h3>
store_blocks = wrapper.find_all("div", recursive=False)

for block in store_blocks:
    name_tag = block.find("h3")
    if not name_tag:
        continue  # skip non-store divs

    store_name = name_tag.get_text(strip=True)

    address_parts = []
    for sib in name_tag.find_next_siblings():
        if sib.name == "p" and "store_simple_hours" in sib.get("class", []):
            break
        if sib.name == "div":
            text = sib.get_text(" ", strip=True)
            if text:
                address_parts.append(text)

    if not address_parts:
        continue

    store_address = ", ".join(address_parts)
    stores.append({
        "Store Name": store_name,
        "Address": store_address
    })

# Convert to pandas DataFrame
df = pd.DataFrame(stores)

# Export to CSV
df.to_csv("farmboy_stores.csv", index=False, encoding="utf-8-sig")

print(f"Scraped {len(stores)} stores")
print("Saved to farmboy_stores.csv")
