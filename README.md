# Dynamic Quotes Scraper (Playwright & Python)

A robust, automated web scraper built with Python and Playwright to crawl dynamic, JavaScript-rendered web pages. It handles multi-page navigation seamlessly and exports structured data into clean JSON and UTF-8 encoded CSV formats.

## Key Features
* **JavaScript Execution:** Uses Playwright to render dynamic single-page content that traditional HTTP GET requests miss.
* **Automated Pagination:** Detects and interacts with dynamic "Next" page buttons until all pages are fully scraped.
* **Dual Output Formats:** Automatically exports structured records into both `quotes.json` and `quotes.csv`.
* **Clean Data Formatting:** Formats tag arrays into comma-separated strings for immediate spreadsheet compatibility.

## Tech Stack
* **Language:** Python 3.8+
* **Browser Automation:** Playwright (Firefox Engine)
* **Data Serialization:** Python `json` & `csv` standard libraries

## Repository Structure
```text
├── playwright_quotes_scraper.py   # Main automation script
├── quotes.csv                      # Sample exported CSV dataset
├── quotes.json                     # Sample exported JSON dataset
└── README.md                       # Project documentation
