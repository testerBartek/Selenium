from selenium import webdriver

class IEDriverWindows():
    def testMethod(self):
        driver = webdriver.Ie(executable_path="C:\\Users\\nn\\PycharmProjects\\drivers\\IEDriverServer.exe")
        driver.get("http://www.google.com")

ieObject = IEDriverWindows()
ieObject.testMethod()
