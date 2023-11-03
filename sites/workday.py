from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from information import *
from utilities import *


def workday(driver):
  wait(3)
  driver.find_element(By.CSS_SELECTOR,"#root div div div.css-8atqhb div div div div.css-shnk6d div:nth-child(1) div button").click()
  print("Declined Cookies")

  wait(1)
  driver.find_element(By.XPATH,"//a[@data-automation-id='adventureButton']").click()
  print("Click Apply")

  wait(1)
  driver.find_element(By.XPATH, "//a[@data-automation-id='applyManually']").click()
  print("Click Apply Manually")

  wait(4)
  try:
    driver.find_element(By.LINK_TEXT, "Next").click()
  except NoSuchElementException:
    print("No CV prompt")
    pass
  else:
    print("Skipped CV upload")
    wait(5)

  try:
    driver.find_element(By.XPATH, "//div[@data-automation-id='previousWorker']/div[2]/div/input").click()
  except NoSuchElementException:
    print("No previous employment radio")
    pass
  else:
    print("'No' selected for previous employment")

  try:
    driver.find_element(By.XPATH, "//button[@data-automation-id='legalNameSection_title']").send_keys(Keys.ENTER + "Mr" + Keys.ENTER)
  except NoSuchElementException:
    print("No Prefix Option")
    pass

  wait(0.5)
  driver.find_element(By.XPATH, "//input[@data-automation-id='legalNameSection_firstName']").send_keys(information["firstName"])
  driver.find_element(By.XPATH, "//input[@data-automation-id='legalNameSection_lastName']").send_keys(information["lastName"])
  driver.find_element(By.XPATH, "//input[@data-automation-id='addressSection_addressLine1']").send_keys(information["address1"])
  driver.find_element(By.XPATH, "//input[@data-automation-id='addressSection_postalCode']").send_keys(information["postCode"])
  driver.find_element(By.XPATH, "//input[@data-automation-id='email']").send_keys(information["email"])

  try:
    driver.find_element(By.XPATH, "//button[@data-automation-id='phone-device-type']").send_keys(Keys.ENTER + "Mobile" + Keys.ENTER)
  except NoSuchElementException:
    print("No Device Type Option")
    pass

  driver.find_element(By.XPATH, "//input[@data-automation-id='phone-number']").send_keys(information["phoneNumber"])
  driver.find_element(By.XPATH, "//button[@data-automation-id='bottom-navigation-next-button']").click()
  print("Next Page")

  wait(3)
  for i in range(len(education)):
    e = education[i]
    print(e["fieldOfStudy"])
    driver.find_elements(By.XPATH, "//input[@data-automation-id='school']")[i].send_keys(e["university"])
    driver.find_elements(By.XPATH, "//button[@data-automation-id='degree']")[i].send_keys(Keys.ENTER + "B" + Keys.ENTER)
    driver.find_elements(By.XPATH, "//div[@data-automation-id='formField-field-of-study']/div/div/div/div/div[1]/div[1]/input")[i].send_keys(e["fieldOfStudy"] + Keys.ENTER)
    if e["fieldOfStudy"] == "Mechanical Engineering":
      driver.find_element(By.XPATH, "//div[@data-automation-label='Mechanical Engineering']").click()

    driver.find_elements(By.XPATH, "//input[@data-automation-id='gpa']")[i].send_keys(e["overallGPA"])
    driver.find_elements(By.XPATH, "//div[@data-automation-id='formField-startDate']/div/div/div[2]/div/div/input")[i].send_keys(e["from"])
    driver.find_elements(By.XPATH, "//div[@data-automation-id='formField-endDate']/div/div/div[2]/div/div/input")[i].send_keys(e["to"])
    if i < len(education) - 1:
      driver.find_element(By.XPATH, "//button[@data-automation-id='Add Another']").click()
    wait(1)

  wait(1)
  driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH, "//button[@aria-label='Add Languages']"))
  wait(1)
  driver.find_element(By.XPATH, "//button[@data-automation-id='language']").send_keys(Keys.ENTER + "English" + Keys.ENTER)
  driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH, "//input[@data-automation-id='nativeLanguage']"))
  driver.find_element(By.XPATH, "//button[@data-automation-id='languageProficiency-0']").send_keys(Keys.ENTER + "h" + Keys.ENTER)
  driver.find_element(By.XPATH, "//button[@data-automation-id='languageProficiency-1']").send_keys(Keys.ENTER + "h" + Keys.ENTER)
  driver.find_element(By.XPATH, "//button[@data-automation-id='languageProficiency-2']").send_keys(Keys.ENTER + "h" + Keys.ENTER)

  for skill in information["skills"]:
    wait(0.5)
    driver.find_element(By.XPATH, "//div[@data-automation-id='formField-skillsPrompt']/div/div/div/div/div[1]/input").send_keys(skill + Keys.ENTER)
    wait(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    print(skill)

  driver.find_element(By.XPATH, "//input[@data-automation-id='file-upload-input-ref']").send_keys("C:\\Users\\ryanl\\Desktop\\Resume-CV.docx")
  driver.find_element(By.XPATH, "//input[@data-automation-id='linkedinQuestion']").send_keys(information["linkedin"])
  driver.find_element(By.XPATH, "//button[@data-automation-id='bottom-navigation-next-button']").click()
  wait(3)

  driver.find_element(By.XPATH, "//button[@data-automation-id='d3608a04c8ef1001f4464a1d10740000']").send_keys(Keys.ENTER + "Y" + Keys.ENTER) # can start internship on date
  driver.find_element(By.XPATH, "//button[@data-automation-id='d3608a04c8ef1001f4464a1d10740003']").send_keys(Keys.ENTER + "Y" + Keys.ENTER) # graduate in penultimate year
  driver.find_element(By.XPATH, "//button[@data-automation-id='d3608a04c8ef1001f4464ab6b4cc0001']").send_keys(Keys.ENTER + "Y" + Keys.ENTER) # right to work in the uk
  driver.find_element(By.XPATH, "//button[@data-automation-id='0b28199847c61001f4dd055f57c80000']").send_keys(Keys.ENTER + "N" + Keys.ENTER) # sponsorship
  driver.find_element(By.XPATH, "//button[@data-automation-id='d3608a04c8ef1001f4464ab6b4cc0004']").send_keys(Keys.ENTER + "UK Passport" + Keys.ENTER) # right to work
  driver.find_element(By.XPATH, "//button[@data-automation-id='d3608a04c8ef1001f4464ab6b4cc0008']").send_keys(Keys.ENTER + "N" + Keys.ENTER) # applied for more than 1?
  driver.find_element(By.XPATH, "//button[@data-automation-id='d3608a04c8ef1001f4464b506d3e0002']").send_keys(Keys.ENTER + "N" + Keys.ENTER) # worked for partners?
  driver.find_element(By.XPATH, "//button[@data-automation-id='d3608a04c8ef1001f4464b506d3e0006']").send_keys(Keys.ENTER + "N" + Keys.ENTER) # RAP
  driver.find_element(By.XPATH, "//button[@data-automation-id='d3608a04c8ef1001f4464bea263a0002']").send_keys(Keys.ENTER + "N" + Keys.ENTER) # know anyone in the company
  driver.find_element(By.XPATH, "//button[@data-automation-id='bottom-navigation-next-button']").click()
  wait(3)

  driver.find_element(By.XPATH, "//button[@data-automation-id='76311b02889e0101962e6526022d0000']").send_keys(Keys.ENTER + "Routine" + Keys.ENTER) # occupation of main income earner when 14
  driver.find_element(By.XPATH, "//button[@data-automation-id='76311b02889e0101962e65bfe0510008']").send_keys(Keys.ENTER + "Independent or fee-paying school, where" + Keys.ENTER) # type of school at 11-16
  driver.find_element(By.XPATH, "//button[@data-automation-id='76311b02889e0101962e65bfe0510009']").send_keys(Keys.ENTER + "I don't know" + Keys.ENTER) # free school meals
  driver.find_element(By.XPATH, "//button[@data-automation-id='76311b02889e0101962e65bfe051000a']").send_keys(Keys.ENTER + "Y" + Keys.ENTER) # parents attend uni
  driver.find_element(By.XPATH, "//button[@data-automation-id='bottom-navigation-next-button']").click()
  wait(3)

  driver.find_element(By.XPATH, "//button[@data-automation-id='gender']").send_keys(Keys.ENTER + "Male" + Keys.ENTER)
  driver.find_element(By.XPATH, "//input[@data-automation-id='dateSectionMonth-input']").send_keys(information["birthMonth"])
  driver.find_element(By.XPATH, "//input[@data-automation-id='dateSectionDay-input']").send_keys(information["birthDay"])
  driver.find_element(By.XPATH, "//input[@data-automation-id='dateSectionYear-input']").send_keys(information["birthYear"])
  driver.find_element(By.XPATH, "//button[@data-automation-id='maritalStatus']").send_keys(Keys.ENTER + "Single" + Keys.ENTER)
  driver.find_element(By.XPATH, "//div[@data-automation-id='formField-ethnicities']/div/div/div/div/div[1]/input").send_keys("Asian - Other" + Keys.ENTER)
  driver.find_element(By.XPATH, "//button[@data-automation-id='sexualOrientation']").send_keys(Keys.ENTER + "Hetero" + Keys.ENTER)
  driver.find_element(By.XPATH, "//button[@data-automation-id='pronoun']").send_keys(Keys.ENTER + "He" + Keys.ENTER)
  driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH, "//input[@data-automation-id='agreementCheckbox']"))
  driver.find_element(By.XPATH, "//button[@data-automation-id='bottom-navigation-next-button']").click()
  wait(3)

  # driver.find_element(By.XPATH, "//button[@data-automation-id='bottom-navigation-next-button']").click()
  return
