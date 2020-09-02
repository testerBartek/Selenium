from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class ElementState():

    def isEnabled(self):
        base_url = "http://www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        time.sleep(5)

        e1 = driver.find_element(By.NAME, "q")
        e1State = e1.is_enabled() #True for enabled and False for disabled
        print("E1 is Enabled? -> " + str(e1State))

        e1.send_keys("test")
        e1.send_keys(Keys.ENTER)


gc = ElementState()
gc.isEnabled()
