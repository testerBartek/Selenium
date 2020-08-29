from selenium import webdriver

class RunFFTests():
    def testMethod(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\nn\\PycharmProjects\\drivers\\geckodriver.exe")
        driver.get("http://www.google.com")

ff = RunFFTests()
ff.testMethod()
