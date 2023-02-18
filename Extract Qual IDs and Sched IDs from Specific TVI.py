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

# Set the path to the Microsoft Edge webdriver
service = EdgeService(executable_path="C:\Program Files\msedgedriver.exe")

# Create an instance of the Edge class using the service
driver = webdriver.Edge(service=service)


TVIIDNo = "5152"          #ID OF THE TARGET INSTITUTION


#The link for the list of all qualifications
website = "https://t2mis.tesda.gov.ph/POAdmin/SchoolQualifications/" + TVIIDNo

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

tablerows = table.find_elements("tag name","a")

QualIDNos = [] #Variable to store the extracted schedule id nos.

for tablerow in tablerows:
    href = tablerow.get_attribute("href")
    if "Schedule" in href:
        # Get the numbers in the end of the href text and store as text value
        QIDNo = re.findall(r'\d+', href)[-1]
        QualIDNos.append(QIDNo)

CountofQualIDNos = len(QualIDNos)



#===========================================================================
#===========================================================================


#===========================================================================
#===========================================================================
# ConsoSchedIDNos = []
SchedIDNos = []  # empty variable to append

with tqdm(total=CountofQualIDNos) as pbar:
    #Get all the SCHEDULE ID in a given qualification and store in a list
    for QualIDNo in QualIDNos:   #Temp disable for single QUALIFICATION ONLY

        # QualIDNo = "46916"  #Use this code when you want to go directly into the SCHEDULE IDs
                                #Disable after using

        #The link for the list of all schedules in a certain qualification
        website2 = "https://t2mis.tesda.gov.ph/POAdmin/QualificationSchedules/" + QualIDNo

        # Navigate to the website
        driver.get(website2)

        # ===================================================================
        # First determine how many pages are there?
        page_nos = [1] #Page 1 was added so it will be the default value if there are qualifications with no more than 1 page
        liTags = driver.find_elements("tag name","li")

        for liTag in liTags:
            # print(liTag.text)
            aTag = liTag.find_element("tag name","a")
            # for aTag in aTags:
            href = aTag.get_attribute("href")
            mystr = str(href)
            if mystr.find("?page=") != -1:
                page = re.findall(r'\d+', mystr)[-1]
                page_nos.append(page)
                #If the code does not find any href, the page_nos will be empty. Hence, there should be a default value of 1
        # ===================================================================

        for a in page_nos: #For each page it will extract all the specific Schedule ID No
            website2nextpage = website2 + "?page=" + str(a)
            driver.get(website2nextpage)
            # EXTRACT THE SCHEDULE ID NOs
            # Locate the table
            table = driver.find_element("tag name","table")

            # Locate the table rows
            trs = table.find_elements("xpath","//tr")

            Yr = "2021"

            for tr in trs:
                if Yr in tr.text:
                    # Locate the element with tag "a" within the table
                    links = tr.find_elements("tag name","a")
                    # Locate the element with attribute name "href" and attribute value "Enroll"
                    for link in links:
                        href = link.get_attribute("href")
                        if "Enroll" in href:
                            # Get the numbers in the end of the href text and store as text value
                            numbers = re.findall(r'\d+', href)[-1]
                            SchedIDNos.append(numbers)
        sleep(0.1)
        pbar.update(1)

print(SchedIDNos)
CountofSchedIDNos = len(SchedIDNos)
mystr = str(CountofSchedIDNos)
Prompt = "There are " + mystr + " Schedule ID Numbers"
print(Prompt)
    #===========================================================================
    #===========================================================================

driver.quit()
