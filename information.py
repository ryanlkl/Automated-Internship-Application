from decouple import config

information = {
  "firstName": config("FIRSTNAME"),
  "lastName": config("LASTNAME"),
  "email": config("EMAIL"),
  "address1": config("ADDRESS1"),
  "postCode": config("POSTCODE"),
  "phoneNumber": config("PHONENUMBER"),
  "linkedin": config("LINKEDIN"),
  "birthDay": config("BIRTHDAY"),
  "birthMonth": config("BIRTHMONTH"),
  "birthYear": config("BIRTHYEAR"),
  "skills": ["Python","HTML","CSS","MATLAB","C","Flask","React","Pandas","Bootstrap","Selenium Webdriver","BeautifulSoup","Detail-Oriented","Communication"],
  "location": "Birmingham, United Kingdom"
}

education = [
  {
    "university": "University of Birmingham",
    "degree": "Bachelor's",
    "fieldOfStudy": "Mechanical Engineering",
    "overallGPA": "3.7",
    "from": "2021",
    "to": "2025"
  },
  {
    "university": "University of Birmingham",
    "degree": "Bachelor's",
    "fieldOfStudy": "Computer Science",
    "overallGPA": "3.7",
    "from": "2023",
    "to": "2024"
  },]
