import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, JavascriptException

def wait(seconds):
  time.sleep(seconds)
  return

def load(driver,route):
   return WebDriverWait(driver,5,EC.presence_of_element_located((By.XPATH,route)))

def find_element_by_xpath(driver, tag, attribute_text, *keys, click=False, path="",index=None):
    try:
        if index:
           element = driver.find_elements(By.XPATH, f"//{tag}[@{attribute_text}]{path}")[index]
        else:
          element = driver.find_element(By.XPATH, f"//{tag}[@{attribute_text}]{path}")
    except NoSuchElementException:
        print(f"NoSuchElementException: {tag}[@{attribute_text}]")
        return None
    except ElementNotInteractableException:
        print(f"ElementNotInteractableException: {tag}[@{attribute_text}]")
        return None
    except IndexError:
       print("IndexError")
       return None

    # Check if the element is an input and already has a value
    if (tag == "input" or path.endswith("/input")) and element.get_attribute("value"):
        return None

    # Check if the element is a textarea and already has text
    if (tag == "textarea" or path.endswith("/textarea")) and element.text:
        return None

    # Click the element if 'click' is set to True
    if click:
        element.click()
        return

    # Send keys to the element if 'keys' are provided
    if keys:
        print(keys)
        element.send_keys(keys)
        return

    return element



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
