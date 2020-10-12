from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class HomeOptions(BasePage):

 def click_on_games(self):
     wait = WebDriverWait(self.driver, 10)
     # Waiting until the next process comes up
     element=self.driver.find_element_by_xpath("//android.widget.TextView[@text='Games']")
     if webdriver.wait.until(element.is_displayed()):
      element.click()
     else:
         print("element not found")


