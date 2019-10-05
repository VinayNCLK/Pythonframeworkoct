from base.selenium_webdriver import SeleniumWebDriver
import utilities.customlogger as cl
import logging
from selenium.webdriver.common.by import By
import time

class CreateuserPO(SeleniumWebDriver):
    log = cl.customLogger(logLevel=logging.INFO)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators values
    _firstnametxtbx_id="createUserPanel_firstNameField"
    _middlenametxtbx_id="createUserPanel_middleNameField"
    _lastnametxtbx_id="createUserPanel_lastNameField"
    _emailtxtbx_id="createUserPanel_emailField"
    _usernametxtbx_id="createUserPanel_usernameField"
    _password_id="createUserPanel_passwordField"
    _retypepwd_id="createUserPanel_passwordCopyField"
    _departmentdrpdwn_xpath="//div[contains(text(),'-- department not assigned --')]"
    _select_hrandfinances_xpath1="//div[contains(text(),'-- new department --')]/following-sibling::div[contains(text(),"
    _select_hrandfinances_xpath2 = ")]"
    _clickoncreate_xpath="//div[contains(text(),'Create User')]"

    def createnewuser(self,firstname,middlename,lastname,emailid,username,pwd,retypepwd,dept):
        self.webdriverwait_elementclickable(self._firstnametxtbx_id,20,2,"id")
        self.sendData(firstname,self._firstnametxtbx_id,"id")
        self.sendData(middlename,self._middlenametxtbx_id,"id")
        self.sendData(lastname,self._lastnametxtbx_id,"id")
        self.sendData(emailid,self._emailtxtbx_id,"id")
        self.sendData(username,self._usernametxtbx_id,"id")
        self.sendData(pwd,self._password_id,"id")
        self.clear(self._retypepwd_id, "id")
        self.sendData(retypepwd,self._retypepwd_id,"id")
        self.click(self._departmentdrpdwn_xpath,"xpath")
        print(self._select_hrandfinances_xpath1+"'"+dept+"'"+self._select_hrandfinances_xpath2)
        self.driver.find_element(By.XPATH,self._select_hrandfinances_xpath1+"'"+dept+"'"+self._select_hrandfinances_xpath2).click()
        self.click(self._clickoncreate_xpath,"xpath")
        self.clear(self._retypepwd_id, "id")
        self.sendData(retypepwd, self._retypepwd_id, "id")
        self.click(self._clickoncreate_xpath,"xpath")
