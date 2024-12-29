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
- Includes rate limiting to be respectful to TradeMe's servers
- Error handling for robust operation

## Output

The script will create a CSV file named `trademe_cars.csv` containing the scraped data with the following columns:
- title
- price
- location
- scraped_date

## Note

Please be mindful of TradeMe's terms of service and robots.txt when using this scraper. Adjust the sleep time between requests if needed.
