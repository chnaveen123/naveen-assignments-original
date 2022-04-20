
from bs4 import BeautifulSoup
import requests

html_txt = requests.get("https://www.keepinspiring.me/famous-quotes/")
print(html_txt)

soup = BeautifulSoup(html_txt.text, "lxml")

res = soup.findAll("cite")
for ct in res:
    print(ct.text)


print("-" * 40)


quotes = soup.findAll("blockquote")
for quote in quotes:
    print(quote.text)