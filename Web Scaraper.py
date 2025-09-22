from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for i in range(len(quotes)):
    print(f"Quote: {quotes[i].text}")
    print(f"Author: {authors[i].text}")
    print("---")