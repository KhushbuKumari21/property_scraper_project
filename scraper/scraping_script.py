from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options if needed
chrome_options = webdriver.ChromeOptions()

# Create the WebDriver with ChromeDriverManager and Chrome options
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)



# URL of the 99acres page you want to scrape
url = '99acres.com/search/property/buy/hyderabad-all?city=38&preference=S&area_unit=1&res_com=R'

# Load the webpage
driver.get(url)

# Wait for the page to load (you might need to adjust the time)
driver.implicitly_wait(10)

# Get the page source
page_source = driver.page_source

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract property details
property_name = soup.find('span', class_='property-name').text
property_cost = soup.find('span', class_='property-cost').text
property_type = soup.find('span', class_='property-type').text
property_area = soup.find('span', class_='property-area').text

# Print property details (you can store them in variables or a database)
print(f'Property Name: {property_name}')
print(f'Property Cost: {property_cost}')
print(f'Property Type: {property_type}')
print(f'Property Area: {property_area}')

# Close the WebDriver
driver.quit()
