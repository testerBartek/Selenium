from selenium import webdriver


class FindByXpathCss():

    def test(self):
        baseUrl = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elementByXpath = driver.find_element_by_xpath("//*[@id='email']")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        elementByCss = driver.find_element_by_css_selector("#content > div > div > div > div._8esl > h2")

        if elementByCss is not None:
            print("We found an element by Css")

gc = FindByXpathCss()
gc.test()