from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from information import *
from utilities import *

def smartrecruiters(driver):
  wait(3)
  driver.find_element(By.XPATH, "//a[@id='st-apply']").click()
  input("Press Enter when Capcha is finished: ")
