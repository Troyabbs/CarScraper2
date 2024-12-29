from car_browser import CarScraper
import time

def get_user_input():
    print("\nEnter car details:")
    make = input("Car make (e.g., mazda): ").strip().lower()
    model = input("Car model (e.g., mx-5): ").strip().lower()
    return make, model

def create_search_url(make, model):
    base_url = 'https://www.trademe.co.nz/a/motors/cars'
    return f"{base_url}/{make}/{model}/search?sort_order=motorspriceasc"

def run_scraper():
    make, model = get_user_input()
    web = create_search_url(make, model)
    path = r'c:/Users/troya/Downloads/CarScraper2/chromedriver.exe'

    print(f"\nStarting scraper for {make.upper()} {model.upper()}...")
    scraper = CarScraper(web, path)
    scraper.start_driver()
    cars = scraper.get_car_data()
    
    # Create filename with car details
    filename = f"{make}_{model}_cars.csv"
    scraper.save_to_csv(cars, filename)
    scraper.quit_driver()
    print("Done!")

while True:
    try:
        run_scraper()
        print("\nWaiting 1 hour before next run...")
        time.sleep(3600)
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(60)  # Wait 1 minute before retrying
    print("\nPress Ctrl+C to stop the program")

if __name__ == "__main__":
    run_scraper()