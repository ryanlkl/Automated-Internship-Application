driver.find_element(By.XPATH, "//div[@data-field='cover_letter']/div[2]/button").click()
  autoit.control_focus("Open", "File Name")
  autoit.control_set_text("Open", "File Name", "C:\\Users\\ryanl\\Desktop\\Cover-Letter.docx")
  autoit.control_click("Open", "Button2")