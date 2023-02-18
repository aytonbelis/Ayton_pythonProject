from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import re
import pyautogui
import time
import tkinter as tk
import tkinter.messagebox as mb

# Set the path to the Microsoft Edge webdriver
service = EdgeService(executable_path="C:\Program Files\msedgedriver.exe")

# Create an instance of the Edge class using the service
driver = webdriver.Edge(service=service)


website = "https://t2mis.tesda.gov.ph/POAdmin/QualificationSchedules/9465"

# Navigate to the website
driver.get(website)

#input email
email_field = driver.find_element_by_name("Email")
email_field.send_keys("etdoniego@tesda.gov.ph")

#input password
password_field = driver.find_element_by_name("Password")
password_field.send_keys("7fraters")

#locate and press login button
login_button = driver.find_element_by_xpath("//input[@type='submit']")
login_button.click()

# Wait for the page to load
driver.implicitly_wait(40)

#===========================================================================
# EXTRACT THE QUALIFICATION IDs
# Locate the table
table = driver.find_element_by_tag_name("table")

# Locate the element with tag "a" within the table
links = table.find_elements_by_tag_name("a")

serialnumbers = [] #empty variable to append


# Locate the element with attribute name "href" and attribute value "Enroll"
for link in links:
    href = link.get_attribute("href")
    if "Enroll" in href:
        # Get the numbers in the end of the href text and store as text value
        numbers = re.findall(r'\d+', href)[-1]
        serialnumbers.append(numbers)

#Locate the table rows
tds = table.find_elements_by_xpath("//td")


DateStarted = []

for a in serialnumbers:
    print(a)





# Close the webdriver
driver.quit()
