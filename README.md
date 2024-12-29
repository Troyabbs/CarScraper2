# TradeMe Car Scraper

This Python script scrapes car listings from TradeMe's motor vehicle section.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the scraper:
```bash
python car_scraper.py
```

## Features

- Scrapes car listings from TradeMe
- Extracts title, price, and location information
- Saves data to a CSV file
- Error handling for robust operation

## Output

The script will create a CSV file named `trademe_cars.csv` containing the scraped data with the following columns:
- title
- price
- location
- kilometers
- link

## Note

Adjust the sleep time between requests and minimum price if needed.
