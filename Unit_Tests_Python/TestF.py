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
driver.get(hlp.url_main_page)
driver.maximize_window()

# Wait until button 'Login' will be clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Log In')]")))
# Click on battle LogIn
driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()

# Switch from 'Sign Up' to 'Log In'
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log In')]")))
driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]").click()
# Set wait until button 'Log In with Email' will be visible and click on it
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Log in with Email']")))
driver.find_element(By.XPATH, "//span[normalize-space()='Log in with Email']").click()
# Clear and fill fields
# wait.until(EC.element_to_be_clickable((By.XPATH, "input_input_emailInput_SM_ROOT_COMP790")))
driver.find_element(By.XPATH, "//input[@id='input_input_emailInput_SM_ROOT_COMP783']").click()
driver.find_element(By.XPATH, "//input[@id='input_input_emailInput_SM_ROOT_COMP783']").clear()
driver.find_element(By.XPATH, "//input[@id='input_input_emailInput_SM_ROOT_COMP783']").send_keys(hlp.user_email)
print("Email done")
driver.find_element(By.XPATH, "//input[@id='input_input_passwordInput_SM_ROOT_COMP783']").click()
driver.find_element(By.XPATH, "//input[@id='input_input_passwordInput_SM_ROOT_COMP783']").clear()
driver.find_element(By.XPATH, "//input[@id='input_input_passwordInput_SM_ROOT_COMP783']").send_keys(hlp.user_password)
print("Password done")
driver.find_element(By.XPATH, "//*[@class='uDW_Qe wixui-button PlZyDq'][@aria-disabled='true']").click()