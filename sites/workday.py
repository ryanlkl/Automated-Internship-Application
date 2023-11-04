from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from information import *
from utilities import *


def workday(driver,url):
  # Decline Cookies
  wait(3)
  find_element_by_xpath(driver,"button","data-automation-id='legalNoticeDeclineButton'",click=True)
  print("Declined Cookies")

  # Log in/Apply
  if "login" in url:
    find_element_by_xpath(driver,"input","data-automation-id='email'",information["email"])
    find_element_by_xpath(driver,"input","data-automation-id='password'",information["password"])
    find_element_by_xpath(driver,"div","data-automation-id='click_filter'",Keys.ENTER,Keys.ENTER)
  else:
    find_element_by_xpath(driver,"a","data-automation-id='adventureButton'",click=True)
    print("Click Apply")

  # Apply Manually
  wait(5)
  find_element_by_xpath(driver,"a","data-automation-id='applyManually'",click=True)

  # Basic Information
  wait(4)
  driver.find_element(By.XPATH, "//button[@data-automation-id='legalNameSection_title']").send_keys(Keys.ENTER + "Mr" + Keys.ENTER)
  find_element_by_xpath(driver,"div","data-automation-id='previousWorker'",path="/div[2]/div/input",click=True)
  find_element_by_xpath(driver,"button","data-automation-id='legalNameSection_title'",Keys.ENTER,information["title"],Keys.ENTER)
  find_element_by_xpath(driver,"input","data-automation-id='legalNameSection_firstName'",information["firstName"])
  find_element_by_xpath(driver,"input","data-automation-id='legalNameSection_lastName'",information["lastName"])
  find_element_by_xpath(driver,"input","data-automation-id='addressSection_addressLine1'",information["address1"])
  find_element_by_xpath(driver,"input","data-automation-id='addressSection_addressLine2'",information["address2"])
  find_element_by_xpath(driver,"input","data-automation-id='addressSection_city'",information["city"])
  find_element_by_xpath(driver,"input","data-automation-id='addressSection_postalCode'",information["postCode"])
  find_element_by_xpath(driver,"input","data-automation-id='email'",information["email"])
  find_element_by_xpath(driver,"button","data-automation-id='phone-device-type'",Keys.ENTER,"Mobile",Keys.ENTER)
  find_element_by_xpath(driver,"input","data-automation-id='phone-number'",information["phoneNumber"])
  find_element_by_xpath(driver,"button","data-automation-id='bottom-navigation-next-button'",click=True)
  print("Next Page")

  # Experience Section
  fromCount = 0
  toCount = 0
  add_another_button = 0
  wait(3)
  if find_element_by_xpath(driver,"div","data-automation-id='workExperienceSection'"):

    for i in range(len(workExperience)):
      w = workExperience[i]
      print(w["title"])
      print(i)
      print(len(driver.find_elements(By.XPATH, "//input[@data-automation-id='jobTitle']")))
      driver.find_elements(By.XPATH, "//input[@data-automation-id='jobTitle']")[i].send_keys(w["title"])
      driver.find_elements(By.XPATH, "//input[@data-automation-id='company']")[i].send_keys(w["company"])
      driver.find_elements(By.XPATH, "//input[@data-automation-id='location']")[i].send_keys(w["location"])
      if w["workCurrently"]:
        execute_click(driver,driver.find_elements(By.XPATH, "//input[@data-automation-id='currentlyWorkHere']")[i])
      driver.find_elements(By.XPATH, "//input[@data-automation-id='dateSectionMonth-input']")[2*i].send_keys(w["fromMonth"])
      driver.find_elements(By.XPATH, "//input[@data-automation-id='dateSectionYear-input']")[2*i].send_keys(w["fromYear"])
      fromCount += 2
      if not w["workCurrently"]:
        driver.find_elements(By.XPATH, "//input[@data-automation-id='dateSectionMonth-input']")[(2*i)+1].send_keys(w["toMonth"])
        driver.find_elements(By.XPATH, "//input[@data-automation-id='dateSectionYear-input']")[(2*i)+1].send_keys(w["toYear"])
        toCount += 2
      driver.find_elements(By.XPATH, "//textarea[@data-automation-id='description']")[i].send_keys(w["description"])
      if i < len(workExperience) - 1:
        driver.find_elements(By.XPATH, "//button[@data-automation-id='Add Another']")[add_another_button].click()
      wait(1)
    add_another_button += 1
    wait(3)

  # Education Section
  if find_element_by_xpath(driver,"div","data-automation-id='educationSection'"):
    for i in range(len(education)):
      e = education[i]
      print(e["fieldOfStudy"])
      driver.find_elements(By.XPATH, "//input[@data-automation-id='school']")[i].send_keys(e["university"])
      driver.find_elements(By.XPATH, "//button[@data-automation-id='degree']")[i].send_keys(Keys.ENTER + "B" + Keys.ENTER)
      driver.find_elements(By.XPATH, "//div[@data-automation-id='formField-field-of-study']/div/div/div/div/div[1]/div[1]/input")[i].send_keys(e["fieldOfStudy"] + Keys.ENTER)
      if e["fieldOfStudy"] == "Mechanical Engineering":
        find_element_by_xpath(driver,"div","data-automation-label='Mechanical Engineering'",click=True)

      driver.find_elements(By.XPATH, "//input[@data-automation-id='gpa']")[i].send_keys(e["overallGPA"])
      driver.find_elements(By.XPATH, "//div[@data-automation-id='formField-startDate']/div/div/div[2]/div/div/input")[fromCount].send_keys(e["from"])
      fromCount += 1
      driver.find_elements(By.XPATH, "//div[@data-automation-id='formField-endDate']/div/div/div[2]/div/div/input")[toCount].send_keys(e["to"])
      toCount += 1
      if i < len(education) - 1:
        driver.find_elements(By.XPATH, "//button[@data-automation-id='Add Another']")[1].click()
      wait(1)

  # Language Section
  wait(1)
  if find_element_by_xpath(driver,"div","data-automation-id='languageSection'"):
    execute_click(driver,find_element_by_xpath(driver,"button","aria-label='Add Languages'"))
    wait(1)
    find_element_by_xpath(driver,"button","data-automation-id='language'",Keys.ENTER,"English",Keys.ENTER)
    execute_click(driver,find_element_by_xpath(driver,"input","data-automation-id='nativeLanguage'"))
    for i in range(5):
      find_element_by_xpath(driver,"button",f"data-automation-id='languageProficiency-{i}'",Keys.ENTER)
      if driver.find_elements(By.XPATH,f"//ul[@role='listbox']/li/div")[3].text == "A - Beginner":
        find_element_by_xpath(driver,"button",f"data-automation-id='languageProficiency-{i}'",Keys.ENTER,"C",Keys.ENTER)
      elif driver.find_elements(By.XPATH,f"//ul[@role='listbox']/li/div")[3].text == "High":
        find_element_by_xpath(driver,"button",f"data-automation-id='languageProficiency-{i}'",Keys.ENTER,"h",Keys.ENTER)

  # Skill Section
  if find_element_by_xpath(driver,"div","data-automation-id='skillSection'"):
    for skill in information["skills"]:
      wait(0.5)
      find_element_by_xpath(driver,"div","data-automation-id='formField-skillsPrompt'",skill,Keys.ENTER,path="/div/div/div/div/div[1]/input")
      wait(1)
      ActionChains(driver).send_keys(Keys.ENTER).perform()
      print(skill)

  find_element_by_xpath(driver,"input","data-automation-id='file-upload-input-ref'","C:\\Users\\ryanl\\Desktop\\Resume-CV.docx")
  find_element_by_xpath(driver,"input","data-automation-id='linkedinQuestion'",information["linkedin"])
  find_element_by_xpath(driver,"button","data-automation-id='bottom-navigation-next-button'",click=True)
  wait(3)

  # Application Questions
  find_element_by_xpath(driver,"button","data-automation-id='d3608a04c8ef1001f4464a1d10740000'",Keys.ENTER,information["startInternshipOnDate"],Keys.ENTER) # can start internship on date
  find_element_by_xpath(driver,"button","data-automation-id='d3608a04c8ef1001f4464a1d10740003'",Keys.ENTER,information["graduateInYear"],Keys.ENTER) # graduate in penultimate year
  find_element_by_xpath(driver,"button","data-automation-id='d3608a04c8ef1001f4464ab6b4cc0001'",Keys.ENTER,information["workInUK"],Keys.ENTER) # right to work in the uk
  find_element_by_xpath(driver,"button","data-automation-id='0b28199847c61001f4dd055f57c80000'",Keys.ENTER,information["needSponsorship"],Keys.ENTER) # sponsorship
  find_element_by_xpath(driver,"button","data-automation-id='d3608a04c8ef1001f4464ab6b4cc0004'",Keys.ENTER,information["RTWDocument"],Keys.ENTER) # right to work
  find_element_by_xpath(driver,"button","data-automation-id='d3608a04c8ef1001f4464ab6b4cc0008'",Keys.ENTER,information["appliedForMultiple"],Keys.ENTER) # applied for more than 1?
  find_element_by_xpath(driver,"button","data-automation-id='d3608a04c8ef1001f4464b506d3e0002'",Keys.ENTER,information["workedForPartners"],Keys.ENTER) # worked for partners?
  find_element_by_xpath(driver,"button","data-automation-id='d3608a04c8ef1001f4464b506d3e0006'",Keys.ENTER,information["RAP"],Keys.ENTER) # RAP
  find_element_by_xpath(driver,"button","data-automation-id='d3608a04c8ef1001f4464bea263a0002'",Keys.ENTER,information["knowAnyoneInCompany"],Keys.ENTER) # know anyone in the company
  find_element_by_xpath(driver,"button","data-automation-id='bottom-navigation-next-button'",click=True)
  wait(3)

  find_element_by_xpath(driver,"button","data-automation-id='76311b02889e0101962e6526022d0000'",Keys.ENTER,information["mainIncome"],Keys.ENTER) # occupation of main income earner when 14
  find_element_by_xpath(driver,"button","data-automation-id='76311b02889e0101962e65bfe0510008'",Keys.ENTER,information["secondarySchool"],Keys.ENTER) # type of school at 11-16
  find_element_by_xpath(driver,"button","data-automation-id='76311b02889e0101962e65bfe0510009'",Keys.ENTER,information["freeMeals"],Keys.ENTER) # free school meals
  find_element_by_xpath(driver,"button","data-automation-id='76311b02889e0101962e65bfe051000a'",Keys.ENTER,information["parentsAttendUni"],Keys.ENTER) # parents attend uni
  find_element_by_xpath(driver,"button","data-automation-id='bottom-navigation-next-button'",click=True)
  wait(3)

  find_element_by_xpath(driver,"button","data-automation-id='gender'",Keys.ENTER,information["gender"],Keys.ENTER)
  find_element_by_xpath(driver,"input","data-automation-id='dateSectionMonth-input'",information["birthMonth"])
  find_element_by_xpath(driver,"input","data-automation-id='dateSectionDay-input'",information["birthDay"])
  find_element_by_xpath(driver,"input","data-automation-id='dateSectionYear-input'",information["birthYear"])
  find_element_by_xpath(driver,"button","data-automation-id='maritalStatus'",Keys.ENTER,information["maritalStatus"],Keys.ENTER)
  find_element_by_xpath(driver,"div","data-automation-id='formField-ethnicities'",information["ethnicity"],Keys.ENTER,path="/div/div/div/div/div[1]/input")
  find_element_by_xpath(driver,"button","data-automation-id='sexualOrientation'",Keys.ENTER,information["orientation"],Keys.ENTER)
  find_element_by_xpath(driver,"button","data-automation-id='pronoun'",Keys.ENTER,information["pronoun"],Keys.ENTER)
  execute_click(driver,find_element_by_xpath(driver,"input","data-automation-id='agreementCheckbox'"))
  find_element_by_xpath(driver,"button","data-automation-id='bottom-navigation-next-button'",click=True)
  wait(3)

  # find_element_by_xpath(driver,"button","data-automation-id='bottom-navigation-next-button'",click=True)
  return
