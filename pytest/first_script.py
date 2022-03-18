from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pdb  # python debugger

driver = webdriver.Firefox()
driver.get("http://demostore.supersqa.com/")

print(driver.title)

pdb.set_trace()
