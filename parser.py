import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

rows = []
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
        rows.append({"title": title, "price": price})

    print(f"Сторінка {page} готова")
    time.sleep(1)


for row in rows:
    row["price"] = float(row["price"].replace("£", ""))


df = pd.DataFrame(rows)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")
df.to_excel("books.xlsx", index=False)
print(df.head())
print(len(df))
