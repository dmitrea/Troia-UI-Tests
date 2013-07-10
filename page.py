import selenium.webdriver.support.ui as ui
from selenium import webdriver
from settings import Settings
import random
import string
import time


class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def getUrl(self):
        return self.driver.current_url

    def findElements(self, idMode, idValue):
        try:
            webElements = None
            if (idMode == 'id'):
                webElements = self.driver.find_elements_by_id(idValue)
            elif (idMode == 'xpath'):
                webElements = self.driver.find_elements_by_xpath(idValue)
            elif (idMode == 'name'):
                webElements = self.driver.find_elements_by_name(idValue)
            elif (idMode == 'linkText'):
                webElements = self.driver.find_elements_by_link_text(idValue)
            elif (idMode == 'partialLinkText'):
                webElements = self.driver.find_elements_by_partial_link_text(idValue)
            elif (idMode == 'tagName'):
                webElements = self.driver.find_elements_by_tag_name(idValue)
            elif (idMode == 'className'):
                webElements = self.driver.find_elements_by_class_name(idValue)
            elif (idMode == 'cssSelector'):
                webElements = self.driver.find_elements_by_css_selector(idValue)
            else:
                webElements = None
            hover = webdriver.ActionChains(self.driver).move_to_element(webElements[0])
            hover.perform()
            return webElements
        except:
            print 'Cannot find elements %s %s' %(idMode, idValue)

    def findElement(self, idMode, idValue):
        webElement = None
        try:
            if (idMode == 'id'):
                webElement = self.driver.find_element_by_id(idValue)
            elif (idMode == 'xpath'):
                webElement = self.driver.find_element_by_xpath(idValue)
            elif (idMode == 'name'):
                webElement = self.driver.find_element_by_name(idValue)
            elif (idMode == 'linkText'):
                webElement = self.driver.find_element_by_link_text(idValue)
            elif (idMode == 'partialLinkText'):
                webElement = self.driver.find_element_by_partial_link_text(idValue)
            elif (idMode == 'tagName'):
                webElement = self.driver.find_element_by_tag_name(idValue)
            elif (idMode == 'className'):
                webElement = self.driver.find_element_by_class_name(idValue)
            elif (idMode == 'cssSelector'):
                webElement = self.driver.find_element_by_css_selector(idValue)
            else:
                webElement = None
            hover = webdriver.ActionChains(self.driver).move_to_element(webElement)
            hover.perform()
        except:
            print 'Cannot find element %s %s' %(idMode, idValue)
        return webElement

    def setText(self, idMode, idValue, text):
        elem = self.findElement(idMode, idValue)
        elem.send_keys(text)

    def selectListValue(self, idMode, idValue, value):
        elem = self.findElement(idMode, idValue)
        for option in elem.find_elements_by_tag_name('option'):
            if option.text.upper() == value.upper():
                option.click()

    def clickButton(self, idMode, idValue):
        element = self.findElement(idMode, idValue)
        element.click()

    def waitUntilElementIsPresent(self, idMode, idValue):
        wait = ui.WebDriverWait(self.driver, Settings.webElementTimeOut)
        if (idMode == 'id'):
            wait.until(lambda driver: self.driver.find_element_by_id(idValue))
        elif (idMode == 'tagName'):
            wait.until(lambda driver: self.driver.find_element_by_tag_name(idValue))
        elif (idMode == 'className'):
            wait.until(lambda driver: self.driver.find_element_by_class_name(idValue))
