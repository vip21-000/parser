English | [Українська](README.uk.md)

# Sandbox: Books to Scrape Parser

A educational scraper created to practice basic web scraping skills on the [Books to Scrape](http://books.toscrape.com/) test site.

## What the Script Collects
The script iterates through the book catalog and extracts basic information about each publication:
* Book title
* Price
* Rating (number of stars)
* Link to the book page

## Result Example
![books_preview.png](books_preview.png)

## How to Run
1. Make sure your virtual environment is activated and dependencies from the root directory are installed.
2. Run the script:
   ```bash
   python sandbox_books_toscrape/parser.py
