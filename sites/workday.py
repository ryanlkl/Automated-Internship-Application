from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from information import *
from utilities import *

class WorkDay():
  def __init__(self,driver):
    self.driver = driver

  def next_page(self):
    print("Next")
    return find_element_by_xpath(self.driver,"button","data-automation-id='bottom-navigation-next-button'",click=True)

  def decline_cookies(self):
    return find_element_by_xpath(self.driver,"button","data-automation-id='legalNoticeDeclineButton'",click=True)

  def click_apply(self):
    find_element_by_xpath(self.driver,"a","data-automation-id='adventureButton'",click=True)
    return

  def apply_manually(self):
    find_element_by_xpath(self.driver,"a","data-automation-id='applyManually'",click=True)
    return

  def register(self):
    section = find_element_by_xpath(self.driver,"div","data-automation-id='signInContent'")

    if not section:
      print("No Sign In Section")
      return

    # Log in
    # find_element_by_xpath(self.driver,"button","data-automation-id='createAccountLink'",click=True)

    find_element_by_xpath(self.driver,"input","data-automation-id='email'",information["email"])
    find_element_by_xpath(self.driver,"input","data-automation-id='password'",information["password"])
    find_element_by_xpath(self.driver,"input","data-automation-id='verifyPassword'",information["password"])
    find_element_by_xpath(self.driver,"div","data-automation-id='click_filter'",Keys.ENTER,Keys.ENTER)
    return

  def my_information(self):
    section = find_element_by_xpath(self.driver, "div","data-automation-id='contactInformationPage'")
    if not section:
      print("No Information Page")
      return
    find_element_by_xpath(self.driver,"div","data-automation-id='formField-sourcePrompt'",Keys.ENTER,"Linkedin",Keys.ENTER,path="/div/div/div/div[1]/div[1]/input")
    execute_click(self.driver,find_element_by_xpath(self.driver,"div","data-automation-id='previousWorker'",path="/div[2]/div/input")) # Selecting No
    find_element_by_xpath(self.driver,"button","data-automation-id='legalNameSection_title'",Keys.ENTER,information["title"],Keys.ENTER)
    find_element_by_xpath(self.driver,"input","data-automation-id='legalNameSection_firstName'",information["firstName"])
    find_element_by_xpath(self.driver,"input","data-automation-id='legalNameSection_lastName'",information["lastName"])
    find_element_by_xpath(self.driver,"input","data-automation-id='addressSection_addressLine1'",information["address1"])
    find_element_by_xpath(self.driver,"input","data-automation-id='addressSection_addressLine2'",information["address2"])
    find_element_by_xpath(self.driver,"input","data-automation-id='addressSection_city'",information["city"])
    find_element_by_xpath(self.driver,"button","data-automation-id='addressSection_countryRegion'",Keys.ENTER,information["county"],Keys.ENTER)
    find_element_by_xpath(self.driver,"input","data-automation-id='addressSection_postalCode'",information["postCode"])
    find_element_by_xpath(self.driver,"input","data-automation-id='email'",information["email"])
    find_element_by_xpath(self.driver,"button","data-automation-id='phone-device-type'",Keys.ENTER,"Mobile",Keys.ENTER)
    find_element_by_xpath(self.driver,"input","data-automation-id='phone-number'",information["phoneNumber"])
    return

  def work_experience(self):
    section = find_element_by_xpath(self.driver,"div","data-automation-id='workExperienceSection'")
    if not section:
      print("No Work Experience Section")
      return
    add = find_element_by_xpath(section,"button","data-automation-id='Add'")
    if add:
      add.send_keys(Keys.ENTER)
    for i in range(len(workExperience)):
        w = workExperience[i]
        find_element_by_xpath(section,"input","data-automation-id='jobTitle'",w["title"],index=i)
        find_element_by_xpath(section,"input","data-automation-id='company'",w["company"],index=i)
        find_element_by_xpath(section,"input","data-automation-id='location'",w["location"],index=i)
        if w["workCurrently"]:
          execute_click(self.driver,find_element_by_xpath(self.driver,"input","data-automation-id='currentlyWorkHere'",index=i))
        find_element_by_xpath(section,"input","data-automation-id='dateSectionMonth-input'",w["fromMonth"],index=2*i)
        find_element_by_xpath(section,"input","data-automation-id='dateSectionYear-input'",w["fromYear"],index=2*i)
        if not w["workCurrently"]:
          find_element_by_xpath(section,"input","data-automation-id='dateSectionMonth-input'",w["toMonth"],index=(2*i)+1)
          find_element_by_xpath(section,"input","data-automation-id='dateSectionYear-input'",w["toYear"],index=(2*i)+1)
        find_element_by_xpath(section,"textarea","data-automation-id='description'",w["description"],index=i)
        if find_element_by_xpath(section,"div",f"data-automation-id='workExperience-{len(workExperience)}'"):
          print("found")
          break
        if i < len(workExperience) - 1:
          find_element_by_xpath(section,"button","data-automation-id='Add Another'",Keys.ENTER)
        wait(1)
    return

  def education(self):
    section = find_element_by_xpath(self.driver,"div","data-automation-id='educationSection'")
    add = find_element_by_xpath(self.driver,"button","aria-label='Add Education'",Keys.ENTER)
    if add:
      add.send_keys(Keys.ENTER)
    if not section:
      print("No Education Section")
      return
    for i in range(len(education)):
      e = education[i]
      find_element_by_xpath(section,"input","data-automation-id='school'",e["university"],index=i)
      find_element_by_xpath(section,"button","data-automation-id='degree'",Keys.ENTER,"B",Keys.ENTER,index=i)
      find_element_by_xpath(section,"div","data-automation-id='formField-field-of-study'",e["fieldOfStudy"],Keys.ENTER,path="/div/div/div/div/div[1]/div[1]/input",index=i)
      execute_click(self.driver,find_element_by_xpath(self.driver, "div",f"data-automation-label='{e['fieldOfStudy']}'"))
      find_element_by_xpath(section,"div",f"data-automation-label='{e['fieldOfStudy']}'",click=True)
      find_element_by_xpath(section,"input","data-automation-id='dateSectionYear-input'",e["from"],index=2*i)
      find_element_by_xpath(section,"input","data-automation-id='dateSectionYear-input'",e["to"],index=(2*i)+1)
      find_element_by_xpath(section,"input","data-automation-id='gpa'",e["overallGPA"],index=i)
      if find_element_by_xpath(section,"div",f"data-automation-id='education-{len(education)}'"):
        break
      if i < len(education) - 1:
        try:
          find_element_by_xpath(section,"button","aria-label='Add Another Education'", Keys.ENTER)
        except NoSuchElementException:
          find_element_by_xpath(section,"button","data-automation-id='Add Another'",Keys.ENTER)
        except ElementNotInteractableException:
          pass

      wait(1)
    return

  def languages(self):
    section = find_element_by_xpath(self.driver,"div","data-automation-id='languageSection'")
    if not section:
      print("No Languages Section")
      return
    execute_click(self.driver,find_element_by_xpath(self.driver,"button","aria-label='Add Languages'"))
    wait(1)
    find_element_by_xpath(section,"button","data-automation-id='language'",Keys.ENTER,"English",Keys.ENTER)
    execute_click(self.driver,find_element_by_xpath(self.driver,"input","data-automation-id='nativeLanguage'"))
    for i in range(5):
      find_element_by_xpath(section,"button",f"data-automation-id='languageProficiency-{i}'",Keys.ENTER)
      wait(0.5)
      if len(section.find_elements(By.XPATH, "//ul[@role='listbox']/li/div")) > 4 and find_element_by_xpath(self.driver,"ul","role='listbox'",path="/li/div",index=3).text == "A - Beginner":
        find_element_by_xpath(section,"button",f"data-automation-id='languageProficiency-{i}'",Keys.ENTER,"C",Keys.ENTER)
      else:
        find_element_by_xpath(section,"button",f"data-automation-id='languageProficiency-{i}'",Keys.ENTER,"h",Keys.ENTER)
    return

  def skills(self):
    section = find_element_by_xpath(self.driver,"div","data-automation-id='skillsSection'")

    if not section:
      print("No Skills Section")
      return

    for skill in information["skills"]:
      wait(0.5)
      find_element_by_xpath(self.driver,"div","data-automation-id='formField-skillsPrompt'",skill,Keys.ENTER,path="/div/div/div/div/div[1]/input")
      wait(1)
      ActionChains(self.driver).send_keys(Keys.ENTER).perform()
      print(skill)
    return

  def upload_resume(self):
    section = find_element_by_xpath(self.driver,"div","data-automation-id='resumeSection'")
    if not section:
      print("No Resume Section")
      return
    find_element_by_xpath(self.driver,"input","data-automation-id='file-upload-input-ref'","C:\\Users\\ryanl\\Desktop\\Resume-CV.docx")

  def social_network(self):
    section = find_element_by_xpath(self.driver,"div","data-automation-id='socialNetworkSection'")

    if not section:
      print("No Social Media Section")
      return
    find_element_by_xpath(self.driver,"input","data-automation-id='linkedinQuestion'",information["linkedin"])

  def website(self):
    section = find_element_by_xpath(self.driver,"div","data-automation-id='websiteSection'")
    if not section:
      print("No Website Section")
      return
    find_element_by_xpath(section,"input","data-automation-id='website'",information["github"])

  def application_questions(self):
    if not find_element_by_xpath(self.driver,"div","data-automation-id='primaryQuestionnairePage'"):
      print("No Primary Questionnaire Page")
      return
    for question_div in self.driver.find_elements(By.XPATH, "//div[@data-automation-id='primaryQuestionnairePage']/div"):
      question = find_element_by_xpath(question_div,"div","data-automation-id='richText'").text.replace("*","")
      print(question)

      button = find_element_by_xpath(question_div,"button","aria-haspopup='listbox'")
      if button:
        if question not in application_questions:
          input("Click enter after you have manually completed the field:")
          application_questions[question] = button.text
          continue
        button.send_keys(Keys.ENTER, application_questions[question], Keys.ENTER)

      try:
        textarea = question_div.find_element(By.TAG_NAME, "textarea")
      except NoSuchElementException:
        print("No Text Area Tag")
        continue
      else:
        if question not in application_questions:
          input("Click enter after you have manually completed the field:")
          application_questions[question] = textarea.text
          continue
        textarea.send_keys(application_questions[question])


    # find_element_by_xpath(self.driver,"button","data-automation-id='d5f66974c56b1000ad2a15ca82220000'",Keys.ENTER,"Y",Keys.ENTER) # currently attending uni
    # find_element_by_xpath(self.driver,"button","data-automation-id='d5f66974c56b1000ad2a15ca82220003'",Keys.ENTER,"2025",Keys.ENTER) # Graduation  year
    # find_element_by_xpath(self.driver,"button","data-automation-id='d5f66974c56b1000ad2a166432900004'",Keys.ENTER,"N",Keys.ENTER) # Require Sponsorship
    # find_element_by_xpath(self.driver,"button","data-automation-id='d5f66974c56b1000ad2a166432900007'",Keys.ENTER,"N",Keys.ENTER) # Family work at company
    # if find_element_by_xpath(self.driver,"div","data-automation-id='formField-d5f66974c56b1000ad2a166432900003'"): # Earliest Start Date
    #   for i in range(3):
    #     find_element_by_xpath(self.driver,"div","data-automation-id='formField-d5f66974c56b1000ad2a166432900003'",information["date"][i],index=i,path="/div/div/div[3]/div[1]/div/input")
    # find_element_by_xpath(self.driver,"button","data-automation-id='d3608a04c8ef1001f4464a1d10740000'",Keys.ENTER,information["startInternshipOnDate"],Keys.ENTER) # can start internship on date
    # find_element_by_xpath(self.driver,"button","data-automation-id='d3608a04c8ef1001f4464a1d10740003'",Keys.ENTER,information["graduateInYear"],Keys.ENTER) # graduate in penultimate year
    # find_element_by_xpath(self.driver,"button","data-automation-id='d3608a04c8ef1001f4464ab6b4cc0001'",Keys.ENTER,information["workInUK"],Keys.ENTER) # right to work in the uk
    # find_element_by_xpath(self.driver,"button","data-automation-id='0b28199847c61001f4dd055f57c80000'",Keys.ENTER,information["needSponsorship"],Keys.ENTER) # sponsorship
    # find_element_by_xpath(self.driver,"button","data-automation-id='d3608a04c8ef1001f4464ab6b4cc0004'",Keys.ENTER,information["RTWDocument"],Keys.ENTER) # right to work
    # find_element_by_xpath(self.driver,"button","data-automation-id='d3608a04c8ef1001f4464ab6b4cc0008'",Keys.ENTER,information["appliedForMultiple"],Keys.ENTER) # applied for more than 1?
    # find_element_by_xpath(self.driver,"button","data-automation-id='d3608a04c8ef1001f4464b506d3e0002'",Keys.ENTER,information["workedForPartners"],Keys.ENTER) # worked for partners?
    # find_element_by_xpath(self.driver,"button","data-automation-id='d3608a04c8ef1001f4464b506d3e0006'",Keys.ENTER,information["RAP"],Keys.ENTER) # RAP
    # find_element_by_xpath(self.driver,"button","data-automation-id='d3608a04c8ef1001f4464bea263a0002'",Keys.ENTER,information["knowAnyoneInCompany"],Keys.ENTER) # know anyone in the company
    # find_element_by_xpath(self.driver,"button","data-automation-id='76311b02889e0101962e6526022d0000'",Keys.ENTER,information["mainIncome"],Keys.ENTER) # occupation of main income earner when 14
    # find_element_by_xpath(self.driver,"button","data-automation-id='76311b02889e0101962e65bfe0510008'",Keys.ENTER,information["secondarySchool"],Keys.ENTER) # type of school at 11-16
    # find_element_by_xpath(self.driver,"button","data-automation-id='76311b02889e0101962e65bfe0510009'",Keys.ENTER,information["freeMeals"],Keys.ENTER) # free school meals
    # find_element_by_xpath(self.driver,"button","data-automation-id='76311b02889e0101962e65bfe051000a'",Keys.ENTER,information["parentsAttendUni"],Keys.ENTER) # parents attend uni
    # return

  def voluntary_disclosures(self):
    find_element_by_xpath(self.driver,"button","data-automation-id='gender'",Keys.ENTER,information["gender"],Keys.ENTER)
    find_element_by_xpath(self.driver,"input","data-automation-id='dateSectionMonth-input'",information["birthMonth"])
    find_element_by_xpath(self.driver,"input","data-automation-id='dateSectionDay-input'",information["birthDay"])
    find_element_by_xpath(self.driver,"input","data-automation-id='dateSectionYear-input'",information["birthYear"])
    find_element_by_xpath(self.driver,"button","data-automation-id='maritalStatus'",Keys.ENTER,information["maritalStatus"],Keys.ENTER)
    find_element_by_xpath(self.driver,"button","data-automation-id='ethnicity'",information["ethnicity"],Keys.ENTER)
    find_element_by_xpath(self.driver,"input","data-automation-id-prompt='ethnicities'",information["ethnicity"],Keys.ENTER)
    find_element_by_xpath(self.driver,"button","data-automation-id='sexualOrientation'",Keys.ENTER,information["orientation"],Keys.ENTER)
    find_element_by_xpath(self.driver,"button","data-automation-id='pronoun'",Keys.ENTER,information["pronoun"],Keys.ENTER)
    execute_click(self.driver,find_element_by_xpath(self.driver,"input","data-automation-id='agreementCheckbox'"))
    return

  def workday(self):
    # Decline Cookies

    self.decline_cookies()
    self.click_apply()
    # Apply Manually
    wait(5)
    self.apply_manually()
    wait(6)
    self.register()
    # Basic Information
    wait(10)
    self.my_information()
    # Next Page
    self.next_page()
    # Experience Section
    wait(6)
    self.work_experience()
    # Education Section

    self.education()
    # Language Section
    wait(1)
    self.languages()
    # Skill Section
    self.skills()
    # Resume Section
    self.upload_resume()
    # Website Section
    self.website()
    # Social Media Section
    self.social_network()

    # Next Page
    self.next_page()
    # Application Questions
    self.pages = len(self.driver.find_elements(By.XPATH, "//div[@data-automation-id='progressBar']/div"))
    print(self.pages)
    for _ in range(self.pages - 4):
      wait(3)
      self.application_questions()
      self.next_page()

    # Volunatry Disclosures
    self.voluntary_disclosures()
    self.next_page()

    # Submit
    # find_element_by_xpath(self.driver,"button","data-automation-id='bottom-navigation-next-button'",click=True)
    return
