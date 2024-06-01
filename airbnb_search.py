from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

location = "New York City"
checkin_date = "2024-06-01"
checkout_date = "2024-06-05"

def search_airbnb(location, checkin_date, checkout_date):
    driver = webdriver.Chrome()
    driver.get("https://www.airbnb.com/")
    time.sleep(1)
    search_box = driver.find_element(By.NAME, "query")
    search_box.send_keys(location)
    search_box.send_keys(Keys.RETURN)
    
    print(driver.current_url)
    input("Press Enter to close browser...")
    driver.quit()

search_airbnb(location, checkin_date, checkout_date)
