# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMySuite1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_myTest1(self):
    self.driver.get("https://trytestingthis.netlify.app/")
    self.driver.set_window_size(587, 727)
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(1)").click()
    assert self.driver.switch_to.alert.text == "Press a button!"
    self.driver.switch_to.alert.accept()
    self.driver.find_element(By.ID, "fname").click()
    self.driver.find_element(By.ID, "fname").send_keys("Daniel")
    self.driver.find_element(By.ID, "lname").send_keys("Aaron")
    self.driver.find_element(By.ID, "male").click()
    self.driver.find_element(By.ID, "female").click()
    self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
    self.driver.find_element(By.ID, "other").click()
    self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "option").click()
    self.driver.find_element(By.ID, "option").click()
    dropdown = self.driver.find_element(By.ID, "option")
    dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
    self.driver.find_element(By.ID, "option").click()
    dropdown = self.driver.find_element(By.ID, "option")
    dropdown.find_element(By.XPATH, "//option[. = 'Option 3']").click()
    dropdown = self.driver.find_element(By.ID, "owc")
    dropdown.find_element(By.XPATH, "//option[. = 'Option']").click()
    dropdown = self.driver.find_element(By.ID, "owc")
    dropdown.find_element(By.XPATH, "//option[. = 'Option']").click()
    dropdown = self.driver.find_element(By.ID, "owc")
    dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
    dropdown = self.driver.find_element(By.ID, "owc")
    dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
    dropdown = self.driver.find_element(By.ID, "owc")
    dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()
    dropdown = self.driver.find_element(By.ID, "owc")
    dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()
    dropdown = self.driver.find_element(By.ID, "owc")
    dropdown.find_element(By.XPATH, "//option[. = 'Option 3']").click()
    self.driver.find_element(By.ID, "moption").click()
    self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "option3").click()
    self.driver.find_element(By.NAME, "option2").click()
    self.driver.find_element(By.NAME, "Options").click()
    self.driver.find_element(By.NAME, "Options").send_keys("Strawberry")
    self.driver.find_element(By.ID, "favcolor").click()
    self.driver.find_element(By.ID, "favcolor").send_keys("#619898")
    self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
    self.driver.find_element(By.ID, "day").click()
    self.driver.find_element(By.ID, "day").click()
    self.driver.find_element(By.ID, "a").send_keys("100")
    self.driver.find_element(By.ID, "a").click()
    self.driver.find_element(By.ID, "a").click()
    self.driver.find_element(By.ID, "a").click()
    element = self.driver.find_element(By.ID, "a")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    element = self.driver.find_element(By.ID, "a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "a").send_keys("31")
    self.driver.find_element(By.ID, "a").click()
    self.driver.find_element(By.ID, "day").click()
    self.driver.find_element(By.ID, "day").send_keys("2023-11-21")
    self.driver.find_element(By.ID, "quantity").send_keys("1")
    self.driver.find_element(By.ID, "quantity").click()
    self.driver.find_element(By.NAME, "message").click()
    self.driver.find_element(By.NAME, "message").send_keys("The cat was playing in the garden.\\nok ")
    self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.vars["win9134"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win9134"])
    self.driver.switch_to.window(self.vars["root"])
  
