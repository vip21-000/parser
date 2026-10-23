import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

rows = []


for page in range(1, 172):
    try:
        url = f"https://starylev.com.ua/bookstore/page--{page}"
        resp = requests.get(url, timeout=(3.1, 10))
        resp.raise_for_status()
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Помилка: {e}, Номер сторінки: {page}")
        continue


    for book in soup.select("div.product-card"):
        card_name = book.select_one("a[class *='ProductCard_name']")
        title = card_name.text
        author = book.select_one("h4[class*='ProductCard_author']").text
        book_url = f"https://starylev.com.ua{card_name['href']}"

        try:
            price = float(book.select_one("div[class*='ProductCard_regular']").text.strip().replace(" грн", ""))
        except AttributeError:
            price = None

        if price is None:
            in_stock = False
        else:
            in_stock = True

        rows.append({
            "title": title,
            "author": author,
            "price": price,
            "in_stock": in_stock,
            "book_url": book_url
        })

    print(f"Сторінка {page} готова")
    time.sleep(1)
df = pd.DataFrame(rows)
df.to_csv("starylev_catalog.csv", index=False, encoding="utf-8-sig")
df.to_excel("starylev_catalog.xlsx", index=False)
print(df.head())
print(len(df))
