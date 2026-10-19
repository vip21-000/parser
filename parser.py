import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

rows = []

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

for page in range(1, 51):
    try:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        resp = requests.get(url, timeout=(3.1, 10))
        resp.raise_for_status()
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Помилка: {e}, Номер сторінки: {page}")
        continue


    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").text.strip()
        #rating = rating_map[book.p['class'][1]] # хоча можна було б так зробити
        rating = book.p['class']          #
        rating_word = rating[1]           #
        rating = rating_map[rating_word]  #
        book_url = book.h3.a["href"]
        start = "https://books.toscrape.com/catalogue/"
        rows.append({"title": title, "price": price,"rating": rating, "book_url": f"{start}{book_url}"})
    print(f"Сторінка {page} готова")
    time.sleep(1)


for row in rows:
    row["price"] = float(row["price"].replace("£", ""))


df = pd.DataFrame(rows)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")
df.to_excel("books.xlsx", index=False)
print(df.head())
print(len(df))
