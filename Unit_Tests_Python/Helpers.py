# Helpers for Ca-Marketing_Project
import time
import random
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from selenium import webdriver

#driver = webdriver



# URL main page
url_main_page = "https://qasvus.wixsite.com/ca-marketing"

# URL address page
url_address_page = "https://qasvus.wixsite.com/ca-marketing/account/my-addresses"

# Main page Title
main_title = "Home | California Marcketing"

# Address Title
address_title = "My Addres | California Marcketing"

# User Email
user_email = "9012QQQ@gmail.com"

# User Password
user_password = "12AAqqqq@!#"

def delay():
    time.sleep(random.randint(1, 4))


# Verify Pages Title
def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print("Page has", driver.title + " as Page title")







# Check that an elements are present and visible on the Home page
def home_page_elements(driver, text1, text2):
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), text1)]")))
        print(f"Text {text1} is visible!")
    except TimeoutException:
        print("Loading text too much time!")
        driver.get_screenshot_as_file("Loading text too much time.png")
    element = driver.find_element(By.LINK_TEXT, text2)
    if text2 in driver.page_source:
        print(f"LinkText {text2} has attribute " + element.get_attribute("href"))
    else:
        print(f"Page don't have LinkText = {text2}")
    if not text2 in driver.page_source:
        raise Exception("Link Text is wrong!")

