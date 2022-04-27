from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

for i in range(1,5):
    html_text = requests.get("https://www.flipkart.com/search?q=smart+watches+"
                            "samsung&otracker=search&otracker1=search&marketplace=FLIPKART&as-show="
                            "on&as=off&page=" +str(i))
    soup = BeautifulSoup(html_text.text, 'lxml')

    pTbl = PrettyTable(["product", "price"])


    results = soup.findAll("div", class_="_3pLy-c row")

    for result in results:
        prod = result.find("div",class_="_4rR01T")
        price = result.find("div", class_="_30jeq3 _1_WHN1")

        if prod != None:
            pTbl.add_row([prod.text, price.text])

    pTbl.align["product"] = "l"
    pTbl.align["price"] = "r"

    print(pTbl)

