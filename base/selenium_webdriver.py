from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import utilities.customlogger as cl
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumWebDriver:

    log = cl.customLogger(logLevel=logging.INFO)

    def __init__(self, driver):
            self.driver = driver
    #Returns by type
    def getByType(self,locator):
        if locator == "name":
            return By.NAME
        elif locator == "id":
            return By.ID
        elif locator == "class":
            return By.CLASS_NAME
        elif locator == "linktext":
            return By.LINK_TEXT
        elif locator == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        elif locator == "css":
            return By.CSS_SELECTOR
        elif locator == "xpath":
            return By.XPATH
        else:
            self.log.error("Provided locator is wrong "+locator+" Plea"
                           "se provide valid one")
            return False

    def getWebelement(self, locatorvalue ,locator="id"):
        element = None
        try:
            bytype = self.getByType(locator)
            element = self.driver.find_element(bytype, locatorvalue)
            self.log.info("Identified webelement with locator "+locator+
                          "and locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to identify the webelement with locator "
                           ""+locator+"and locator value "+locatorvalue+e)
        return element

    def getWebelements(self, locatorvalue, locator="id"):
        listelement = None
        try:
            bytype = self.getByType(locator)
            listelement = self.driver.find_elements(bytype, locatorvalue)
            self.log.info("Identified webelements with locator " + locator +
                          "and locator value " + locatorvalue)
        except Exception as e:
            self.log.error("Unable to identify the webelements with locator "
                           "" + locator + "and locator value " + locatorvalue + e)
        return listelement

    def isElementPresent(self,locatorvalue ,locator="id"):
        element = self.getWebelement(locatorvalue,locator)
        if element is not None:
            self.log.info("Element found")
            return True
        else:
            self.log.error("Element is not present")
            return False

    def enterUrl(self,url):
        self.driver.get(url)

    def browserNavigations(self, action="back"):
        if action == "back":
            self.log.info("Clicked on back button")
            self.driver.back()
        elif action == "forward":
            self.log.info("Clicked on forward button")
            self.driver.forward()
        elif action == "refresh":
            self.log.info("Refreshed the page")
            self.driver.refresh()
        else:
            self.log.error("Please provide the valid browser action")
            return False

    def setBrowserSize(self, width=500, height=500):
        self.driver.set_window_size(width, height)

    def setBrowserPosition(self, width=500, height=500):
        self.driver.set_window_position(width, height)

    def setBrowserMaxOrMin(self, action="max"):
        if action == "max":
            self.log.info("Maximized the window")
            self.driver.maximize_window()
        elif action == "min":
            self.log.info("Minimized the window")
            self.driver.minimize_window()
        else:
            self.log.error("Please provide the valid action")
            return False

    # Current title of the page
    def getTitle(self):
        title = self.driver.title
        return title

    # Current url of the page
    def getURL(self):
        url = self.driver.current_url
        return url

    def sendData(self,data, locatorvalue ,locator="id"):
        element = self.getWebelement(locatorvalue ,locator)
        if element is not None:
            element.send_keys(data)
            self.log.info("Entered text or data "+data+" into element "+locatorvalue)
        else:
            self.log.error("Unable to send the data")
            return False

    def click(self,locatorvalue ,locator="id"):
        element = self.getWebelement(locatorvalue, locator)
        if element is not None:
            element.click()
            self.log.info("Clicked on web element "+locatorvalue)
        else:
            self.log.error("Unable to click on web element "+locatorvalue)
            return False

    def clear(self, locatorvalue, locator="id"):
        element = self.getWebelement(locatorvalue, locator)
        if element is not None:
            element.clear()
            self.log.info("Cleared the text from web element " + locatorvalue)
        else:
            self.log.error("Unable to clear the text from web element " + locatorvalue)
            return False

    def getText(self,locatorvalue ,locator="id"):
        element = self.getWebelement(locatorvalue, locator)
        text = None
        if element is not None:
            text =element.text
            self.log.info("Got text "+text+" from web element " + locatorvalue)
        else:
            self.log.error("Unable to get the text from web element " + locatorvalue)
        return text

    def selectOptionFromDrpDwn(self,option,locatorvalue ,locator="id"):
        element = self.getWebelement(locatorvalue, locator)
        if element is not None:
            s1 = Select(element)
            s1.select_by_visible_text(option)
            self.log.info("Selected "+option+" from drp dwn " + locatorvalue)
        else:
            self.log.error("Unable to select option from web element " + locatorvalue)

    def deselectalloptions(self,locatorvalue ,locator="id"):
        element = self.getWebelement(locatorvalue, locator)
        if element is not None:
            s1 = Select(element)
            s1.deselect_all()
            self.log.info("De Selected all options from drp dwn " + locatorvalue)
        else:
            self.log.error("Unable to de select option from web element " + locatorvalue)

    def handleframe(self, id=""):
        try:
            self.driver.switch_to.frame(id)
            self.log.info("Swithched to frame "+id)
        except Exception as e:
            self.log.error("Error in handling frame "+e)

    def switchparentframe(self):
        self.driver.switch_to.parent_frame()

    def handlejspopup(self, action = "accept"):
        if action == "accept":
             self.driver.switch_to.alert.accept()
             self.log.info("Clicked on OK button in JS popup")
        elif action == "dismiss":
            self.driver.switch_to.alert.dismiss()
            self.log.info("Clicked on CANCEL button in JS popup")
        else:
            self.log.error("Please provide valid action")
            return False

    def getcurrentwindowid(self):
        currentwindow = self.driver.current_window_handle
        return currentwindow

    def getwindowhandles(self):
        windowhandles = self.driver.window_handles
        return windowhandles

    def switchtowindow(self, windowid):
        self.driver.switch_to.window(windowid)

    def webdriverwait_elementclickable(self, locatorvalue, waittime=20, poll_freq=2 ,locator="id"):
        try:
            wait = WebDriverWait(self.driver, waittime, poll_freq,
                        ignored_exceptions=[NoSuchElementException,
                    ElementNotInteractableException,
                                            ElementNotVisibleException])
            bytype = self.getByType(locator)
            wait.until(EC.element_to_be_clickable(
                (bytype, locatorvalue)))
            self.log.info("Waited for element "+str(waittime))
        except Exception as e:
            self.log.error("Unable to wait for element "+str(e))

    def webdriverwait_titlecontains(self,title, waittime=20, poll_freq=2):
        try:
            wait = WebDriverWait(self.driver, waittime, poll_freq,
                        ignored_exceptions=[NoSuchElementException,
                    ElementNotInteractableException,
                                            ElementNotVisibleException])
            wait.until(EC.title_contains(title))
            self.log.info("Waited for title "+str(waittime))
        except Exception as e:
            self.log.error("Unable to wait for title "+str(e))

    def webdriverwait_urlcontains(self, url, waittime=20, poll_freq=2):
        try:
            wait = WebDriverWait(self.driver, waittime, poll_freq,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotInteractableException,
                                                     ElementNotVisibleException])
            wait.until(EC.title_contains(url))
            self.log.info("Waited for url " + str(waittime))
        except Exception as e:
            self.log.error("Unable to wait for url " + str(e))

    def mouseover(self,locatorvalue ,locator="id"):
        try:
            element = self.getWebelement(locatorvalue, locator)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except Exception as e:
            self.log.error("Unable to mouse over on element "+locatorvalue)


    def mouseover_click(self,locatorvalue ,locator="id"):
        try:
            element = self.getWebelement(locatorvalue, locator)
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()
            self.log.info("Mouse over on element "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to mouse over on element "+locatorvalue)

    def scrollpage(self, x="0", y="500"):
        self.driver.execute_script("window.scrollBy("+x+","+y+");")
