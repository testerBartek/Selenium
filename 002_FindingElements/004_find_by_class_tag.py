from selenium import webdriver


class FindByClassTag():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing The Element")

        if elementByClassName is not None:
            print("We found an element by Class Name")

#it's really rare - maybe sometimes to title or header
        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text

        if elementByTagName is not None:
            print("We found an element by Tag Name and the text on element is: " + text)

gc = FindByClassTag()
gc.test()
