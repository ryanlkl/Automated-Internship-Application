from selenium import webdriver
from sites.workday import WorkDay
from sites.smartrecruiters import smartrecruiters
from sites.greenhouse import greenhouse
from utilities import *

add = True
urls = []
while add:
  url = input("\nPlease enter the URL for the application or hit 'Enter' to continue:\n")
  if url.lower() == "":
    break
  urls.append(url)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)

if __name__ == "__main__":

  for url in urls:
    driver.get(url)
    driver.implicitly_wait(1)

    if "myworkdayjobs" in url:
      workday = WorkDay(driver)
      workday.workday()
    elif "smartrecruiters" in url:
      smartrecruiters(driver)
    elif "greenhouse" in url:
      greenhouse(driver)

    input("Please confirm your details then press 'Enter'")
