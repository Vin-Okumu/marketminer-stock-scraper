from src.scrape import fetch_page

url="your yahoo url"

soup=fetch_page(url)

print(soup.title.text)