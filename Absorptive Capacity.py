from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import pyautogui
import time
import tkinter as tk
import tkinter.messagebox as mb

from tqdm import tqdm
from time import sleep

import pandas as pd

# Set the path to the Microsoft Edge webdriver
service = EdgeService(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")

# Create an instance of the Edge class using the service
driver = webdriver.Edge(service=service)


# TVIIDNo = "3594"          #ID OF THE TARGET INSTITUTION


#The link for the list of all qualifications
website = "https://t2mis.tesda.gov.ph/POAdmin/ScholarshipAbsorptiveInventory/2023"

# Navigate to the website
driver.get(website)

#input email
email_field = driver.find_element("name","Email")
email_field.send_keys("etdoniego@tesda.gov.ph")

#input password
password_field = driver.find_element("name","Password")
password_field.send_keys("7fraters")

#locate and press login button
login_button = driver.find_element("xpath","//input[@type='submit']")
login_button.click()

# Wait for the page to load
driver.implicitly_wait(40)

#===========================================================================
#===========================================================================
    #These codes are for the extraction of QUALIFICATION ID

# Locate the table
table = driver.find_element("tag name","table")

rows = table.find_elements("tag name","tr")
# cells = rows.find_elements("tag name","td")

data1 = []
with tqdm(total=100) as pbar:
    for row in rows:
        # print(row)
        data1.append(row)
        sleep(0.1)
        pbar.update(1)

    data1len = len(data1)
    # print(data1len)

    data = []
with tqdm(total=data1len) as pbar:
    for row in rows:
        cols = row.find_elements("tag name","td")
        cols = [col.text for col in cols]
        data.append(cols)
        sleep(0.1)
        pbar.update(1)

driver.quit()

# create a DataFrame from the list of lists
df = pd.DataFrame(data)

# write the DataFrame to an Excel file
df.to_excel("table.xlsx", index=False)
df = pd.read_excel("table.xlsx")
