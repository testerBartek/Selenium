from selenium import webdriver


class FindByIdName():

    def test(self):
        baseUrl = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elementbyId = driver.find_element_by_id("email")

        if elementbyId is not None:
            print("We found an element by Id")

        elementByName = driver.find_element_by_name("pass")

        if elementByName is not None:
            print("We found an element by Name")

#We should remember about Dynamic IDs - it's impossible to check.

gc = FindByIdName()
gc.test()
