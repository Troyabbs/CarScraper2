import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from car import Car
import time

class CarScraper:
    def __init__(self, web, driver_path):
        self.web = web
        self.driver_path = driver_path
        self.driver = None

    def start_driver(self):
        # Configure Chrome options to suppress logging
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')  # Only show fatal errors
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')

        # Initialize the driver with our options
        self.driver = webdriver.Chrome(service=Service(self.driver_path), options=chrome_options)

    def clean_price(self, price_str):
        """Convert price string to number, removing '$' and ','"""
        try:
            return float(price_str.replace('$', '').replace(',', ''))
        except:
            return 0

    def get_car_data(self):
        cars_list = []
        max_pages = 3  # Only scrape first 3 pages
        min_price = 2000  # Minimum price threshold

        for page in range(1, max_pages + 1):
            print(f"Scraping page {page} of {max_pages}")
            self.driver.get(f"{self.web}&page={page}")
            time.sleep(2)  # Wait for page to load

            cars = self.driver.find_elements(By.XPATH, '//tg-col[contains(@class,"l-col--has-flex-contents")]')
            if not cars:
                break

            for car in cars:
                try:
                    title = car.find_element(By.XPATH, './/span[contains(@class,"tm-motors-search-card-title__title")]').text
                    price = car.find_element(By.XPATH, './/div[contains(@class,"tm-search-card-price__price")]/div[2]').text
                    
                    # Skip if price is below threshold
                    if self.clean_price(price) < min_price:
                        print(f"Skipping low-priced car: {title} - {price}")
                        continue
                        
                    location = car.find_element(By.XPATH, './/div[contains(@class,"tm-search-card-attributes__attribute-text")]').text
                    kilometers = car.find_element(By.XPATH, './/div[contains(@class, "tm-search-card-attributes__attribute ng-star-inserted")]').text
                    link = car.find_element(By.XPATH, './/a[contains(@class,"tm-tiered-search-card__link o-card")]').get_attribute('href')
                    
                    cars_list.append(Car(title, price, location, kilometers, link))
                    print(f"Found: {title} - {price}")
                except Exception as e:
                    continue

            time.sleep(1)  # Small delay between pages

        print(f"\nTotal cars found (above ${min_price:,}): {len(cars_list)}")
        return cars_list

    def save_to_csv(self, cars, filename):
        if cars:
            df = pd.DataFrame([{
                'Title': car.title, 
                'Price': car.price, 
                'Location': car.location, 
                'Kilometers': car.kilometers, 
                'Link': car.link
            } for car in cars])
            df.to_csv(filename, index=False)
            print(f"Saved {len(cars)} cars to {filename}")

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
