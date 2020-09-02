from selenium import webdriver


class BrowserInteractions():

    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        # Windows Maximize
        driver.maximize_window()
        print("The window is maximize")
        # Open the url
        driver.get(base_url)
        print("The page is load")
        # Get Title
        title = driver.title
        print("Title of the web page is " + title)
        # Get Current Url
        current_url = driver.current_url
        print("Current Url of the web page is: " + current_url)
        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")
        # Open another Url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        current_url = driver.current_url
        print("Current Url of the web page is:" + current_url)
        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        current_url = driver.current_url
        print("Current Url of the web page is:" + current_url)
        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        current_url = driver.current_url
        print("Current Url of the web page is:" + current_url)
        # Get Page Source
        page_source = driver.page_source
        with open('source.html', 'w', encoding="utf-8") as f:
            print(page_source, file=f)
        print("file with page source is saved")
        # Browser Close / Quit
        # driver.close()
        driver.quit()
        print("Every single window of browser is close")


gc = BrowserInteractions()
gc.test()
