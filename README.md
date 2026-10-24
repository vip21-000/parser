English | [Українська](README.uk.md)

# Parser

This repository is a practical portfolio in the field of Web Scraping. 
It shows the evolution of developer skills from simple sandbox scripts to working with complex websites and data structures.

## Repository Structure

* [sandbox_books_toscrape/](sandbox_books_toscrape/) — A learning sandbox based on the test site [Books to Scrape](http://books.toscrape.com/). 
Focuses on basic HTML parsing, selector usage, and saving data.
* [starylev/](starylev/) — A real project for scraping data from the "Old Lion Publishing House" (Stary Lev) website. 
Scrapes a large database (4,775 items), handles pagination, and respects web scraping ethics (robots.txt, delays between requests).

## Quick Start

1. Clone the repository and create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate


2. Install the required dependencies:

pip install -r requirements.txt