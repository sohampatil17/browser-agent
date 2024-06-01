from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_ebay(query):
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com")
    time.sleep(5)
    search_box = driver.find_element(By.ID, "gh-ac")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    print(driver.current_url)
    input("Press Enter to close browser...")
    driver.quit()

search_ebay("IPhone 13 Pro Max")
