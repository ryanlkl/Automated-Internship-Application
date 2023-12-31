from decouple import config

information = {
  "date": ["06","01","2023"],
  "title": config("TITLE"),
  "firstName": config("FIRSTNAME"),
  "lastName": config("LASTNAME"),
  "email": config("EMAIL"),
  "address1": config("ADDRESS1"),
  "address2": config("ADDRESS2"),
  "county": config("COUNTY"),
  "city": config("CITY"),
  "postCode": config("POSTCODE"),
  "phoneNumber": config("PHONENUMBER"),
  "linkedin": config("LINKEDIN"),
  "github": "https://github.com/ryanlkl",
  "birthDay": config("BIRTHDAY"),
  "birthMonth": config("BIRTHMONTH"),
  "birthYear": config("BIRTHYEAR"),
  "skills": ["Python","HTML","CSS","MATLAB","C","Flask","React","Pandas","Bootstrap","Selenium Webdriver","BeautifulSoup","Detail-Oriented","Communication"],
  "location": "Birmingham, United Kingdom",
  "password": config("PASSWORD"),
  "pronoun": config("PRONOUN")
}

workExperience = [
  {
    "title": "Warehouse Operator",
    "company":"Asda",
    "location": "Nottingham",
    "workCurrently": False,
    "fromMonth": "06",
    "fromYear": "2021",
    "toMonth": "09",
    "toYear": "2021",
    "description": "A Warehouse Operative at ASDA is responsible for efficiently handling stock, picking orders, managing inventory, loading/unloading, and ensuring product quality while adhering to strict health and safety regulations. Typical qualifications include prior warehouse experience (though not always required), basic math skills, physical fitness, and attention to detail. Operating forklifts or other equipment may be part of the role. This position imparts knowledge in warehouse operations, inventory management software, health and safety protocols, teamwork, problem-solving, and familiarity with ASDA's products and quality standards, making it valuable for those pursuing a career in logistics and warehousing.",
  },
  {
    "title": "Customer Assistant/Waiter/Kitchen Assistant",
    "company": "Summer Palace Ltd",
    "location": "Nottingham",
    "workCurrently": False,
    "fromMonth": "06",
    "fromYear": "2018",
    "toMonth": "09",
    "toYear": "2021",
    "description": "A Waiter/Kitchen Assistant at a local restaurant plays a pivotal role in providing excellent customer service by greeting patrons, taking orders, maintaining tables, and ensuring a smooth dining experience. They communicate orders between the kitchen and customers, handle billing and payments, and assist kitchen staff with food preparation and maintaining hygiene standards. While prior restaurant or customer service experience is preferred, it's not always required. This position fosters skills in effective communication, teamwork, menu knowledge, basic food safety, and culinary techniques, making it a valuable entry point for those seeking a career in the hospitality industry.",
  },
  {
    "title": "Freelance Video Editor",
    "company": "N/A",
    "location": "Remote",
    "workCurrently": False,
    "fromMonth": "05",
    "fromYear": "2022",
    "toMonth": "06",
    "toYear": "2023",
    "description": "A self-employed freelance video editor is responsible for the comprehensive video editing and post-production process, encompassing tasks like cutting, splicing, adding transitions, effects, and ensuring that the final video aligns with the client's vision. This role demands effective client communication, project management skills to meet deadlines, and the utilization of cutting-edge equipment and software for video editing. Typical experience includes a background in film or media, proficiency in editing software, and strong creative and technical abilities. As a self-starter, video editors must independently manage their business, market their services, and build lasting client relationships while ensuring high-quality video production. This role nurtures knowledge and skills in video editing, project management, software expertise, creativity, adaptability, and entrepreneurial endeavors, making it an avenue for professional growth and artistic development in the video editing industry.",
  },
  {
    "title": "Student Promoter",
    "company": "Hype Collective by Bulla Co",
    "location": "Birmingham",
    "workCurrently": True,
    "fromMonth": "10",
    "fromYear": "2023",
    "toMonth": "11",
    "toYear": "2023",
    "description": "A Student Promoter with Hype Collective by Bulla Co takes on the exciting responsibility of promoting events, parties, and campaigns to their college or university peers. They leverage social media marketing, campus outreach, and their influence within the student community to create buzz and engage the target audience. This role involves actively distributing flyers, organizing promotional activities, and selling event tickets or merchandise while collecting valuable feedback to enhance marketing strategies. Typically current students themselves, Student Promoters gain hands-on experience in event promotion, social media marketing, and understanding the preferences of their peers. They develop strong interpersonal and communication skills, all while balancing promotional activities with their academic commitments, contributing to the success of Hype Collective events and campaigns.",
  },
]

education = [
  {
    "university": "University of Birmingham",
    "degree": "Bachelors",
    "fieldOfStudy": "Mechanical engineering",
    "overallGPA": "3.7",
    "from": "2021",
    "to": "2025"
  },
  {
    "university": "University of Birmingham",
    "degree": "Bachelors",
    "fieldOfStudy": "Computer and Information Science",
    "overallGPA": "3.7",
    "from": "2023",
    "to": "2024"
  },]

application_questions = {
}
