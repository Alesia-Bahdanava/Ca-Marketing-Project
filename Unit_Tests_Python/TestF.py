import time
import random
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from selenium import webdriver
import Helpers as hlp

driver = webdriver.Chrome()
driver.get(hlp.url_account)
driver.maximize_window()
time.sleep(7)

# Wait until button 'Login' will be clickable
wait = WebDriverWait(driver, 10)

driver.quit()