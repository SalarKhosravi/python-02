# What is Web Scraping?
# Web scraping means using a computer program to visit a website and collect information from it — like headlines, prices, pictures, or quotes.


# installation
# pip install requests beautifulsoup4



import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://frenchexam.ir/tcf-french-test/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find products
products = soup.find_all('div', class_="image-none")


# soup.find('h1')  # Gets the first <h1> tag
# soup.find_all('div')  # All <div> tags
# soup.find_all('div', class_='product-box')
# soup.find('div', id='main')
# soup.find('p', class_='description')
# soup.find('a', href='/macbook-pro')
# soup.find_all('img', attrs={'data-src': True})
# soup.find_all('span', string='Apple')

# soup.select('div')
# soup.select('.product')  # like CSS: .class
# soup.select('#main')  # like CSS: #id
# soup.select('div.product span.price')
# soup.select('a[href^="/product/"]')  # Starts with
# soup.select('img[alt*="MacBook"]')   # Contains "MacBook"




# Step 3: Print names and prices
# for product in products:
#     print(product)

# Step 3: Better show
# for index, product in enumerate(products):
#     print(index+1, '- ', product, end='\n\n\n\n')


alts = []
# Find course names
image_divs = soup.find_all('div', class_='image-none')
for div in image_divs:
    img_tag = div.find('img')
    if img_tag and img_tag.has_attr('alt'):
        alts.append(img_tag['alt'])
        print(img_tag['alt'])


print(alts)

# Create a DataFrame with one column named "Alt Text"
df = pd.DataFrame(alts, columns=['Courses'])

# Save DataFrame to CSV (utf-8 encoding to handle special characters)
df.to_csv('alts.csv', index=False, encoding='utf-8')

print("CSV file 'alts.csv' has been created successfully!")

