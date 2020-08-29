from selenium import webdriver
from selenium.webdriver.common.by import By


class UseBy():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found an element by Id")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found an element by XPATH")

        elementByClassName = driver.find_element(By.CLASS_NAME, "table-display")

        if elementByClassName is not None:
            print("We found an element by Class Name")

gc = UseBy()
gc.test()