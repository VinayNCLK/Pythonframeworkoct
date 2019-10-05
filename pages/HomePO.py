from base.selenium_webdriver import SeleniumWebDriver
import utilities.customlogger as cl
import logging

class HomePO(SeleniumWebDriver):
    log = cl.customLogger(logLevel=logging.INFO)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locator values
    _logoutlink = "logoutLink"
    _usertab="//div[text()='USERS']"
    _newuserbtn_xpath="//div[contains(text(),'New User')]"


    def clicklogoutlnk(self):
        self.webdriverwait_elementclickable(self._logoutlink,40,2,"id")
        self.click(self._logoutlink,"id")

    def clickusertab(self):
        self.click(self._usertab,"xpath")

    def clicknewuserbtn(self):
        self.click(self._newuserbtn_xpath,"xpath")


