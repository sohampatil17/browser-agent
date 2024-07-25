from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up the Selenium web driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the Y Combinator companies page
driver.get("https://www.ycombinator.com/companies")

# Wait for the page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div._section_86jzd_146._results_86jzd_326"))
)

# Locate and extract the company elements for the S24 batch
company_elements = driver.find_elements(By.CSS_SELECTOR, "div._section_86jzd_146._results_86jzd_326")

# Extract company information with retry on stale element reference error
company_list = []

for company_element in company_elements:
    retry_count = 3
    while retry_count > 0:
        try:
            name = company_element.find_element(By.CSS_SELECTOR, "h4").text
            details = company_element.find_elements(By.CSS_SELECTOR, "p")
            info = {detail.get_attribute('innerHTML').split(':')[0].strip(): detail.get_attribute('innerHTML').split(':')[1].strip() for detail in details}
            company_list.append({"name": name, **info})
            break
        except Exception as e:
            print(f"Error extracting company: {e}")
            retry_count -= 1
            time.sleep(1)  # Wait a moment before retrying

# Convert the list to a pandas DataFrame
if company_list:
    company_df = pd.DataFrame(company_list)
    print(company_df)
else:
    print("No companies found.")

# Close the web driver
driver.quit()
