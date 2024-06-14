from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os
from together import Together
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
prompt = "Cheap Airbnbs for July 4th in Seatle."


url_response = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[{"role": "user", "content": f"Return me the full url (including https) for the website of the company mentioned and nothing else from this given prompt: {prompt}"}],
)
url = url_response.choices[0].message.content.strip()
print(f"Extracted URL: {url}")

location_response = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[{"role": "user", "content": f"Return me the location or city mentioned and nothing else from this given prompt: {prompt}"}],
)
location = location_response.choices[0].message.content.strip()
print(f"Extracted location: {location}")


# location = "New York City"
checkin_date = "2024-06-15"
checkout_date = "2024-06-17"

def search_airbnb(checkin_date, checkout_date):
    driver = webdriver.Chrome()
    driver.get(url)
    #time.sleep(1)
    
    search_box = driver.find_element(By.XPATH, "//input[@data-testid='structured-search-input-field-query']")
    search_box.send_keys(location)
    search_box.send_keys(Keys.RETURN)
    #time.sleep(1)
    
    # Close any overlay dialogs that might block the search button
    # try:
    #     overlay_close_button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
    #     )
    #     overlay_close_button.click()
    #     time.sleep(2)
    # except:
    #     print("No overlay dialog found or could not close it.")

    search_button = driver.find_element(By.XPATH, "//button[@data-testid='structured-search-input-search-button']")
    driver.execute_script("arguments[0].click();", search_button)  # Use JavaScript click to avoid interception
    #time.sleep(5)
    
    print(driver.current_url)
    input("Press Enter to close browser...")
    driver.quit()

search_airbnb(checkin_date, checkout_date)

# data-testid="structured-search-input-field-guests-button"
# data-testid="calendar-day-07/08/2024"
# data-testid="calendar-day-07/09/2024"
