# Amazon Price Tracker

This project is a simple Python script to track the price of a product on Amazon and log its price history to a CSV file.

## Features
- Fetches the current price of a specified Amazon product using web scraping.
- Extracts the price (whole, fraction, and symbol) from the product page.
- Saves the price, date, and product link to `price_history.csv` for historical tracking.
- Automatically creates the CSV file with headers if it does not exist.

## How It Works
1. The script sends a request to the Amazon product page using custom headers to avoid being blocked.
2. It parses the HTML using BeautifulSoup and locates the price using specific HTML tags/classes.
3. The current price, timestamp, and product link are appended to the CSV file.
4. If the CSV file is new, it writes the header row first.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install dependencies with:
```
pip install requests beautifulsoup4
```

## Usage
1. Activate your virtual environment (optional but recommended):
   ```
   venv\Scripts\activate
   ```
2. Run the script:
   ```
   python price-tracker.py
   ```
3. Check `price_history.csv` for the logged price history.

## Customization
- To track a different product, change the URL in the script.
- The script can be scheduled to run periodically (e.g., with Task Scheduler or cron) for continuous tracking.

## Disclaimer
This script is for educational purposes. Frequent scraping may violate Amazon's terms of service. Use responsibly.
