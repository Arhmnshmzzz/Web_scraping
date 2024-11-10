from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0
for i in range(1, 5):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=PM7POFW3ZNPI&qid=1727169570&sprefix=la%2Caps%2C628&ref=sr_pg_2")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(rf"C:\Users\USER\Desktop\Selenium_Test\Test\data\{query}_{file}.html", "w", encoding="utf-8") as f:
             f.write(d)
             file += 1


time.sleep(2)
driver.close()