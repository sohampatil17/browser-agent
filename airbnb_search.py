from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os
from together import Together

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
prompt = "Cheap Airbnbs for July 4th in Chicago."


url_response = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[{"role": "user", "content": f"Return me the full url for the website of the company mentioned and nothing else from this given prompt: {prompt}"}],
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
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "query")
    search_box.send_keys(location)
    search_box.send_keys(Keys.RETURN)
    
    print(driver.current_url)
    input("Press Enter to close browser...")
    driver.quit()

search_airbnb(checkin_date, checkout_date)