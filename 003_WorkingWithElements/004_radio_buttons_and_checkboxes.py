from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RadioButtonsAndCheckboxes():

    def buttons(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        # DOM input="radio" <- single choose button
        bmwRadioButton = driver.find_element(By.ID, "bmwradio")
        bmwRadioButton.click()

        benzRadioButton = driver.find_element(By.ID, "benzradio")

        hondaRadioButton = driver.find_element(By.ID, "hondaradio")
        hondaRadioButton.click()

        # DOM type"checkbox"
        bmwCheckbox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckbox.click()

        benzCheckbox = driver.find_element(By.ID, "benzcheck")
        benzCheckbox.click()

        hondaCheckbox = driver.find_element(By.ID, "hondacheck")

        # True if selected, False if isn't selected.
        print("BMW radio button is selected? " + str(bmwRadioButton.is_selected()))
        print("Benz radio button is selected? " + str(benzRadioButton.is_selected()))
        print("Honda radio button is selected? " + str(hondaRadioButton.is_selected()))
        print("BMW radio button is selected? " + str(bmwCheckbox.is_selected()))
        print("Benz radio button is selected? " + str(benzCheckbox.is_selected()))
        print("Honda radio button is selected? " + str(hondaCheckbox.is_selected()))


gc = RadioButtonsAndCheckboxes()
gc.buttons()
