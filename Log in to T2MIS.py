from selenium import webdriver

#launch new edge browser
driver = webdriver.Edge()

#navigate to login page
driver.get("https://t2mis.tesda.gov.ph/")

#input email
email_field = driver.find_element_by_name("Email")
email_field.send_keys("etdoniego@tesda.gov.ph")

#input password
password_field = driver.find_element_by_name("Password")
password_field.send_keys("7fraters")

#locate and press login button
login_button = driver.find_element_by_xpath("//input[@type='submit']")
login_button.click()





