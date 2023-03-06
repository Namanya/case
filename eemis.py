import requests
from bs4 import BeautifulSoup

URL = 'https://thenadaka.com/ViewCategory/%20Agriculture'
page = requests.get(URL)

soup = BeautifulSoup(page.content,  'html.parser')

results = soup.find_all(class_= 'listing-item')

for result in results:
    category = result.find('a', class_='category')
    img = result.find('h6')
    print(category.text.strip())
    print(img.text.strip())
    print()