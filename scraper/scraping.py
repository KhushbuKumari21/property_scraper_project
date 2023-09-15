# scraper/scraping.py
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
from scraper.models import Property  # Import your Property model
from django.conf import settings
# property_scraper_app/scraper.py

from .models import Property  # Use a relative import

import time

def scrape_property_data():
    # Configure Selenium WebDriver (Chrome)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in headless mode (without a visible browser window)
    driver = webdriver.Chrome(executable_path=settings.CHROME_DRIVER_PATH, options=chrome_options)

    # Define cities and localities (as you mentioned in the assignment)
    cities = ['Pune', 'Delhi', 'Mumbai', 'Lucknow', 'Agra', 'Ahmedabad', 'Kolkata', 'Jaipur', 'Chennai', 'Bengaluru']
    localities = {
        'Pune': ['Koregaon Park', 'Baner'],
        'Delhi': ['South Delhi', 'North Delhi'],
        # Add localities for other cities as needed
    }

    for city in cities:
        for locality in localities[city]:
            page_number = 1
            while True:
                url = f'https://www.99acres.com/search/property/buy/{city}-all?city=38&preference=S&area_unit=1&res_com=R&locality={locality}&page={page_number}'
                driver.get(url)

                try:
                    # Implement scraping logic using BeautifulSoup
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    
                    # Example scraping logic (modify as per website structure):
                    for property_element in soup.find_all('div', class_='property-listing'):
                        property_name = property_element.find('h2', class_='property-title').text.strip()
                        property_cost = property_element.find('div', class_='property-price').text.strip()
                        property_type = property_element.find('div', class_='property-type').text.strip()
                        property_area = property_element.find('div', class_='property-size').text.strip()
                        property_link = property_element.find('a', class_='property-url')['href']
                        
                        # Create and save Property objects
                        property_data = Property(
                            property_name=property_name,
                            property_cost=property_cost,
                            property_type=property_type,
                            property_area=property_area,
                            property_locality=locality,
                            property_city=city,
                            property_link=property_link
                        )
                        
                        property_data.save()
                
                    # Check for the presence of pagination elements and navigate to the next page
                    next_page_button = driver.find_element_by_css_selector('.pagination-next')
                    if not next_page_button.is_enabled():
                        break  # Break the loop if there's no next page button
                    else:
                        next_page_button.click()
                        page_number += 1
                
                except (TimeoutException, NoSuchElementException, AttributeError) as e:
                    # Handle exceptions appropriately (e.g., log the error)
                    print(f"Error scraping data for {city} - {locality}, Page {page_number}: {str(e)}")
                time.sleep(3)  # Add a delay to avoid overloading the website

    # Close the WebDriver
    driver.quit()

