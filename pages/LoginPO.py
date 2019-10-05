from base.selenium_webdriver import SeleniumWebDriver
import utilities.customlogger as cl
import logging

class LoginPO(SeleniumWebDriver):
    log = cl.customLogger(logLevel=logging.INFO)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locator values
    _usernametxtbx = "username"
    _pwdtxtbx = "//input[@placeholder='Password']"
    _keepmeloggedin = "keepLoggedInCheckBoxContainer"
    _loginbtn = "//div[contains(text(),'Login')]"

    def sendusername(self,username):
        self.sendData(username,self._usernametxtbx,locator="id")

    def sendpwd(self,pwd):
        self.sendData(pwd,self._pwdtxtbx,locator="xpath")

    def clickkeepmeloggedin(self):
        self.click(self._keepmeloggedin,locator="id")

    def loginbtn(self):
        self.click(self._loginbtn,locator="xpath")


    def login(self,username,pwd):
        self.sendusername(username)
        self.sendpwd(pwd)
        self.clickkeepmeloggedin()
        self.loginbtn()

    def errormsgvalidation(self):
        return self.getText(self._errorms_txt,"xpath")
