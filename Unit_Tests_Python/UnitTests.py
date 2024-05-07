import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import Helpers as hlp
import unittest
from selenium.webdriver.common.keys import Keys




class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.minimize_window()
        self.driver.maximize_window()


    def test1_remove_address(self):
        driver = self.driver
        driver.get(hlp.url_main_page)

        #Verify Homepage Title
        hlp.assert_title(driver, "Home | California Marcketing")
        # Check unique el
        hlp.home_page_elements(driver, "LET CALIFORNIA MARKETING GROW YOUR BUSINECS", "CALIFORNIA MARCKETING")

        #Find main img
        if driver.find_element(By.XPATH,"//img[@alt='iot_sq.png']"):
            print("Main img was found")
        else:
            print("Main img LOST")

        #Find text
        if driver.find_element(By.XPATH,"//span[contains(text(),'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')]"):
            print("Main text was found")
        else:
            print("Main text LOST")

        #LogIn in exist accaunt
        hlp.LogIn(driver)



        #Verify title
        #hlp.assert_title(driver, )

        if driver.find_element(By.XPATH,"//div[@class='GVjl6y']//*[name()='svg']"):
            print("Coool")
        else:
            print("Not cool")

        #Go to addresses
        time.sleep(3)
        hlp.Address(driver)
















    def tearDown(self):
        self.driver.quit()



