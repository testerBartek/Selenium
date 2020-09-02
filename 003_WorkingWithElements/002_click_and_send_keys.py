from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndSendKeys():

    def test(self):
        base_url = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        # driver.find_element_by_xpath(By.XPATH, "//a[@href='/sign_in']").click()
        #
        # driver.find_element_by_id(By.ID, "user_email").send_keys("testerbartek@gmail.com")
        #
        # driver.find_element_by_id(By.ID, "user_password").send_keys("1234qwer")
        #
        # time.sleep(3)
        #
        # driver.find_element_by_id(By.ID, "user_email").clear()
        #
        # time.sleep(3)
        #
        # driver.find_element_by_id(By. ID, "user_email").send_keys("tester@gmail.com")

        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()

        driver.implicitly_wait(3)

        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("testek@gmailk.pl")

        password_field = driver.find_element(By.ID, "user_password")
        password_field.send_keys(12345678)

        time.sleep(3)

        email_field.clear()

        time.sleep(3)

        email_field.send_keys("tester@gmail.com")


gc = ClickAndSendKeys()
gc.test()
