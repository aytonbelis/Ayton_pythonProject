from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from bs4 import BeautifulSoup

# Set the path to the Microsoft Edge webdriver
service = EdgeService(executable_path="C:\Program Files\msedgedriver.exe")

# Create an instance of the Edge class using the service
driver = webdriver.Edge(service=service)

# Navigate to the website
driver.get("https://t2mis.tesda.gov.ph/POAdmin/QualificationSchedules/20708")

# Wait for the page to load
driver.implicitly_wait(40)

# Locate all the row elements of the table
rows = driver.find_elements_by_xpath("//table//tr")

# Get the text attribute of each row element and print it
for row in rows:
    print(row.text)

# Close the webdriver
driver.quit()
