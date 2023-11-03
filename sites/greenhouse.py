from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from information import *
from utilities import *
import autoit
import subprocess

def greenhouse(driver):
  wait(2)
  driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(information["firstName"])
  driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys(information["lastName"])
  driver.find_element(By.XPATH, "//input[@id='email']").send_keys(information["email"])
  driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(information["phoneNumber"])
  driver.find_element(By.XPATH, "//auto-complete[@id='job_application_location']/input").send_keys(information["location"])
  wait(0.5)
  driver.find_element(By.XPATH, "//ul[@id='location_autocomplete-items-popup']/li").click()

  driver.find_elements(By.XPATH, "//button[@data-source='attach']")[0].send_keys("C:\\Users\\ryanl\\Desktop\\Resume-CV.docx")

  driver.find_elements(By.XPATH, "//button[@data-source='attach']")[1].send_keys("C:\\Users\\ryanl\\Desktop\\Cover-Letter.docx")

  for i in range(len(education)):
    e = education[i]

    driver.find_element(By.XPATH,f"//div[@id='s2id_education_school_name_{i}']/a").click()
    wait(0.5)
    ActionChains(driver).send_keys(e["university"]).perform()
    wait(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    driver.find_element(By.XPATH, f"//div[@id='s2id_education_degree_{i}']/a").click()
    wait(0.5)
    ActionChains(driver).send_keys(e["degree"]).perform()
    wait(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    driver.find_elements(By.XPATH, "//input[@name='job_application[educations][][end_date][year]']")[i].send_keys(e["to"])

    if i < len(education) - 1:
      driver.find_element(By.XPATH, "//a[@id='add_education']").click()
    wait(0.5)

  driver.find_element(By.XPATH, "//input[@autocomplete='custom-question-linkedin-profile']").send_keys(information["linkedin"])
