import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, JavascriptException

def wait(seconds):
  time.sleep(seconds)

def find_element_by_xpath(driver,tag,attribute_text,*keys,click=False,path=""):
  try:
    element = driver.find_element(By.XPATH, f"//{tag}[@{attribute_text}]{path}")
    if tag == "input" and element.get_attribute("value") != "":
      return
    elif click:
      return element.click()
    if keys:
      print(keys)
      return element.send_keys(keys)
    return element
  except NoSuchElementException:
    print(f"NoSuchElementException: {tag}[@{attribute_text}]")
    return
  except ElementNotInteractableException:
    print(f"ElementNotInteractableException: {tag}[@{attribute_text}]")
    return

def execute_click(driver,element):
  try:
    return driver.execute_script("arguments[0].click();",element)
  except NoSuchElementException:
    print(f"NoSuchElementException: {element}")
    return
  except ElementNotInteractableException:
    print(f"ElementNotInteractableException: {element}")
    return
  except JavascriptException:
    print(f"JavascriptException: {element}")
    return
