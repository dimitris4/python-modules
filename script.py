import requests
from bs4 import BeautifulSoup

page = requests.get('https://github.com/dimitris4/python-modules/blob/master/script.py')

print(page)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())
