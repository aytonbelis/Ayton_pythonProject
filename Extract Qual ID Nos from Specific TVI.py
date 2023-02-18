from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import re
import pyautogui

# Set the path to the Microsoft Edge webdriver
service = EdgeService(executable_path="C:\Program Files\msedgedriver.exe")

# Create an instance of the Edge class using the service
driver = webdriver.Edge(service=service)

# Navigate to the website
driver.get("https://t2mis.tesda.gov.ph/POAdmin/SchoolQualifications/3275")

#input email
email_field = driver.find_element_by_name("Email")
email_field.send_keys("etdoniego@tesda.gov.ph")

#input password
password_field = driver.find_element_by_name("Password")
password_field.send_keys("7fraters")

#locate and press login button
login_button = driver.find_element_by_xpath("//input[@type='submit']")
login_button.click()

#------------------------------------------------


# Locate the table
table = driver.find_element_by_tag_name("table")

tablerows = table.find_elements_by_tag_name("a")

schedserialnumbers = []

for tablerow in tablerows:
    href = tablerow.get_attribute("href")
    if "Schedule" in href:
        # Get the numbers in the end of the href text and store as text value
        schednumbers = re.findall(r'\d+', href)[-1]
        schedserialnumbers.append(schednumbers)




for ssn in schedserialnumbers:
    print(ssn)

# print(schedserialnumbers)

driver.quit()