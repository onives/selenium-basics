from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver = webdriver.Firefox()

# open the url of the site
driver.get("https://nameere-olive-nives.netlify.app/")

driver.implicitly_wait(10)  # implicit wait

print(driver.title)  # get the title of the page
print(driver.current_url)  # return url

# Explicit Wait
project_element_xpath = "//*[@id='responsive-navbar-nav']/div/a[2]"
try:
    project_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, project_element_xpath))
    )
    project_elem.click()
finally:
    time.sleep(4)
    driver.close()
