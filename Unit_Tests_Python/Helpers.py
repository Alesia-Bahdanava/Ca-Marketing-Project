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
user_email = "1Q9012QQQ@gmail.com"

# User Password
user_password = "QQQqq12AAqqqq@!#"

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


# Log In in exist account

def LogIn(driver):
    # Wait until button 'Login' will be clickable
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Log In')]")))
    # Click on battle LogIn
    driver.find_element(By.XPATH,"//span[contains(text(),'Log In')]").click()
    delay()
    # Switch from 'Sign Up' to 'Log In'
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Log In')]")))
    driver.find_element(By.XPATH,"//button[contains(text(),'Log In')]").click()
    # Set wait until button 'Log In with Email' will be visible and click on it
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Log in with Email']")))
    driver.find_element(By.XPATH,"//span[normalize-space()='Log in with Email']").click()
    # Clear and fill fields
    #wait.until(EC.element_to_be_clickable((By.XPATH, "input_input_emailInput_SM_ROOT_COMP790")))
    driver.find_element(By.XPATH,"//input[@id='input_input_emailInput_SM_ROOT_COMP783']").click()
    driver.find_element(By.XPATH, "//input[@id='input_input_emailInput_SM_ROOT_COMP783']").clear()
    driver.find_element(By.XPATH, "//input[@id='input_input_emailInput_SM_ROOT_COMP783']").send_keys(user_email)
    print("Email done")
    driver.find_element(By.XPATH,"//input[@id='input_input_passwordInput_SM_ROOT_COMP783']").click()
    driver.find_element(By.XPATH, "//input[@id='input_input_passwordInput_SM_ROOT_COMP783']").clear()
    driver.find_element(By.XPATH, "//input[@id='input_input_passwordInput_SM_ROOT_COMP783']").send_keys(user_password)
    print("Password done")
    driver.find_element(By.XPATH,"//*[@class='uDW_Qe wixui-button PlZyDq'][@aria-disabled='true']").click()

def Address(driver):
    # Wait and click on user's account button for opening drop-down menu
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='GVjl6y']//*[name()='svg']")))
    # Click drop down menu
    driver.find_element(By.XPATH,"//div[@class='GVjl6y']//*[name()='svg']").click()