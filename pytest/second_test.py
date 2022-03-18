from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pdb  # python debugger

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

current_title = driver.title
expected_title = "Welcome to Python.org"

pdb.set_trace()
