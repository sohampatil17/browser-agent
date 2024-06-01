from selenium import webdriver
import time
import os
from together import Together

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

company_name = "VA Tech"

response = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[{"role": "user", "content": f"Return me the full url for this company's website and nothing else: {company_name}"}],
)

print(response.choices[0].message.content)

driver = webdriver.Chrome()
driver.get(response.choices[0].message.content)
time.sleep(20)
driver.quit()