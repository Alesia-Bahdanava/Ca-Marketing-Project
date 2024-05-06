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

        hlp.home_page_elements(driver, "LET CALIFORNIA MARKETING GROW YOUR BUSINECS", "CALIFORNIA MARCKETING")

        #Verify Homepage Title
#        try:
#            assert driver.title == hlp.main_title
#           print("Current main title is correct:" ,driver.title)
#        except AssertionError:
#            print("Current main title is NOT correct", driver.title)

        #Check unique el
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

        # Scroll page on 800 pixel down to found another element
        driver.execute_script("window.scrollBy(0, 800)")

        #Find products
        if driver.find_element(By.XPATH,"//div[@class='JMHZvW']"):
            print("Products was found")
        else:
            print("Products LOST")

        #

        driver.find_element(By.TAG_NAME,'html').send_keys(Keys.UP)





        # Go to Log in page
        LogIn = driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]")
        LogIn.click()








    def tearDown(self):
        self.driver.quit()



