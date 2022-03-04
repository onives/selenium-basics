from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

import time

# driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver = webdriver.Firefox()

# open the url of the site
driver.get("https://nameere-olive-nives.netlify.app/")

print(driver.title)  # get the title of the page
print(driver.current_url)  # return url
# print(driver.page_source)  # HTML source code for the page

driver.find_element(By.XPATH, "//*[@id='responsive-navbar-nav']/div/a[2]").click()
time.sleep(10)  # wait for a few seconds before closing the browser

driver.close()  # close the browser
