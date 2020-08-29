from selenium import webdriver


class FindByLinkText():

    def test(self):
        baseUrl = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Messenger")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Gam")
        #as a Games

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")

gc = FindByLinkText()
gc.test()
