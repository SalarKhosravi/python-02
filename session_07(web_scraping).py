# 1) Install required libraries (run in terminal, not in Python)
# pip install requests beautifulsoup4 pandas openpyxl

import requests
from bs4 import BeautifulSoup
import pandas as pd

# -------------------------
# 1. FETCH A WEB PAGE
# -------------------------
url = "https://quotes.toscrape.com"  # Example website for scraping practice
response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")

# -------------------------
# 2. PARSE HTML WITH BeautifulSoup
# -------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------
# 3. EXTRACT DATA
# -------------------------
quotes = soup.find_all("div", class_="quote")

data = []
for q in quotes:
    text = q.find("span", class_="text").get_text(strip=True)
    author = q.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]
    
    data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })

# -------------------------
# 4. CREATE A DATAFRAME
# -------------------------
df = pd.DataFrame(data)

# -------------------------
# 5. SAVE TO EXCEL
# -------------------------
df.to_excel("quotes.xlsx", index=False)

print("✅ Scraping completed. Data saved to 'quotes.xlsx'")
