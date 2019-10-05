from selenium import webdriver
import os

class webdriverFactory():
    def __init__(self,browser):
        self.driver_location_chrome = "driverexecutables\\chromedriver.exe"
        self.driver_location_firefox = "driverexecutables\\geckodriver.exe"
        self.driver_location_ie = "driverexecutables\\IEDriverServer.exe"
        os.environ["webdriver.chrome.driver"] = self.driver_location_chrome
        os.environ["webdriver.gecko.driver"] = self.driver_location_firefox
        os.environ["webdriver.ie.driver"] = self.driver_location_ie
        self.browser = browser

    def getWebDriverInstance(self):

        if self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=self.driver_location_chrome)
            print("Execution starts on chrome browser")
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=self.driver_location_firefox)
            print("Execution starts on ff browser")
        else:
            driver = webdriver.Ie(executable_path=self.driver_location_ie)
            print("Execution starts on ie browser")
        driver.get("https://demo.actitime.com/login.do")
        driver.maximize_window()
        driver.implicitly_wait(60)
        return driver

