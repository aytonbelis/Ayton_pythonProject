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
import sys

# Set the path to the Microsoft Edge webdriver
service = EdgeService(executable_path="C:\Program Files\msedgedriver.exe")

# Create an instance of the Edge class using the service
driver = webdriver.Edge(service=service)

website = "https://t2mis.tesda.gov.ph/POAdmin"

# Navigate to the website
driver.get(website)

# input email
email_field = driver.find_element("name", "Email")
email_field.send_keys("etdoniego@tesda.gov.ph")

# input password
password_field = driver.find_element("name", "Password")
password_field.send_keys("7fraters")

# locate and press login button
login_button = driver.find_element("xpath", "//input[@type='submit']")
login_button.click()

# Wait for the page to load
driver.implicitly_wait(40)

# Zoom out the page
pyautogui.keyDown("ctrl")
pyautogui.press("-")
pyautogui.press("-")
pyautogui.press("-")
pyautogui.keyUp("ctrl")


TVIIDNos = [3596, 9052]

# TVIIDNo = "12703"          #ID OF THE TARGET INSTITUTION

for TVIIDNo in TVIIDNos:
    strTVIIDNo = str(TVIIDNo)
    # The link for the list of all qualifications
    website = "https://t2mis.tesda.gov.ph/POAdmin/SchoolQualifications/" + strTVIIDNo

    # Navigate to the website
    driver.get(website)

    # ===========================================================================
    # ===========================================================================
    # These codes are for the extraction of QUALIFICATION ID
    # Locate the table
    table = driver.find_element("tag name", "table")

    tablerows = table.find_elements("tag name", "a")

    QualIDNos = []  # Variable to store the extracted schedule id nos.

    for tablerow in tablerows:
        href = tablerow.get_attribute("href")
        if "Schedule" in href:
            # Get the numbers in the end of the href text and store as text value
            QIDNo = re.findall(r'\d+', href)[-1]
            QualIDNos.append(QIDNo)
    CountofQualIDNos = len(QualIDNos)
    # ===========================================================================
    # ===========================================================================

    # ===========================================================================
    # ===========================================================================
    # Get all the SCHEDULE ID in a given qualification and store in a list

    SchedIDNos = []  # empty variable to append
    trowlist = []  # variable to store the row values
    with tqdm(total=CountofQualIDNos) as pbar:
        for QualIDNo in QualIDNos:  # Temp disable for single QUALIFICATION ONLY

            # QualIDNo = "46916"  #Use this code when you want to go directly into the SCHEDULE IDs
            # Disable after using

            # The link for the list of all schedules in a certain qualification
            website2 = "https://t2mis.tesda.gov.ph/POAdmin/QualificationSchedules/" + QualIDNo

            # Navigate to the website
            driver.get(website2)

            # ===================================================================
            # First determine how many pages are there?
            page_nos = [
                1]  # Page 1 was added so it will be the default value if there are qualifications with no more than 1 page
            liTags = driver.find_elements("tag name", "li")

            for liTag in liTags:
                # print(liTag.text)
                aTag = liTag.find_element("tag name", "a")
                # for aTag in aTags:
                href = aTag.get_attribute("href")
                mystr = str(href)
                if mystr.find("?page=") != -1:
                    page = re.findall(r'\d+', mystr)[-1]
                    page_nos.append(page)
                    # If the code does not find any href, the page_nos will be empty. Hence, there should be a default value of 1
            # ===================================================================
            # SchedIDNos = []  # empty variable to append
            # trowlist = []  # variable to store the row values
            # QualTitles = []
            for a in page_nos:  # For each page it will extract all the specific Schedule ID No
                website2nextpage = website2 + "?page=" + str(a)
                driver.get(website2nextpage)
                # EXTRACT THE SCHEDULE ID NOs FROM THE TABLE ROWS
                # Locate the table
                table = driver.find_element("tag name", "table")

                # Locate the table rows
                trs = table.find_elements("xpath", "//tr")
                Yr = "2023"
                for tr in trs:
                    if Yr in tr.text:
                        # Locate the element with tag "a" within the table
                        links = tr.find_elements("tag name", "a")
                        # Locate the element with attribute name "href" and attribute value "Enroll"
                        for link in links:
                            href = link.get_attribute("href")
                            if "Enroll" in href:
                                # Get the numbers in the end of the href text and store as text value
                                numbers = re.findall(r'\d+', href)[-1]
                                SchedIDNos.append(numbers)
                                # Store all sched id to the variable SchedIDNos
                # ===========================================================================
                # ===========================================================================

                ##Extract the Qualification Title and store to a variable
                # Find the second h4 element - Qualification Title
                QualTitle = driver.find_elements("tag name", "h4")[1]
                toreplace1 = QualTitle.text
                toreplace2 = toreplace1.replace("/", "_")
                toreplace3 = toreplace2.replace("|", "_")
                toreplace4 = toreplace3.replace(":", "_")
                cleanedQualTitle = toreplace4.split("  Nominal")[0]

                ##Extract the values of the table rows except the table header texts and store to a variable
                # Find the table
                tbody = driver.find_element("xpath", "//tbody")
                # Extract all table rows values
                trs = tbody.find_elements("xpath", "//tr")

                for tr in trs:
                    if Yr in tr.text:
                        trtext = tr.text
                        tr1 = trtext.replace("/", "-")
                        tr2 = tr1.replace("Enroll Edit", "")
                        trowlist.append(cleanedQualTitle + "-" + tr2)
            sleep(0.1)
            pbar.update(1)

    print(SchedIDNos)
    CountofSchedIDNos = len(SchedIDNos)
    mystr = str(CountofSchedIDNos)
    Prompt = "There are " + mystr + " Schedule ID Numbers"

    if not SchedIDNos:
        print("The list is empty.")
        # driver.quit()
        # sys.exit()
        continue
    else:
        print(Prompt)
        time.sleep(4)
        # ===========================================================================
        # ===========================================================================
        ##Goto the edge browser work account
        # press and hold
        pyautogui.keyDown('win')

        # press  key
        pyautogui.press('2')
        # press  key
        pyautogui.press('2')

        # release  key
        pyautogui.keyUp('win')
        # ===========================================================================

        CntSchedIDNos = len(SchedIDNos)  # Count the no of values in the list
        # Modified to skip other Qualification IDs
        # iterate over numbers
        for i in range(CntSchedIDNos):
            # move mouse pointer to sked input box
            pyautogui.moveTo(x=113, y=185)
            time.sleep(1)
            # left click image
            pyautogui.doubleClick()
            time.sleep(1)
            pyautogui.press('backspace')
            time.sleep(1)
            pyautogui.typewrite(SchedIDNos[i])
            pyautogui.press('enter')

            # WAIT TIME FOR THE REPORT TO LOAD
            wait = WebDriverWait(driver, 5)
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

            time.sleep(20)  # the time for the report to load

            # move mouse pointer to the Save Button image
            pyautogui.moveTo(x=557, y=247)
            # left click image
            pyautogui.click()

            # move mouse pointer to the Excel option
            pyautogui.moveTo(x=607, y=311)
            # left click image
            pyautogui.click()
            time.sleep(1.5)

            # move to save as
            pyautogui.moveTo(x=1557, y=200)
            time.sleep(12)

            pyautogui.leftClick()  # click save as after  a no of secs

            time.sleep(1)
            pyautogui.press('backspace')

            # Enter the file name
            pyautogui.typewrite(trowlist[i] + "-" + SchedIDNos[i])
            time.sleep(2)

            # pyautogui.moveTo(x=1400, y=779)
            # pyautogui.moveTo(x=1714, y=779)
            # pyautogui.leftClick()

            pyautogui.press('enter')  # This stopped working for unknown reason, temp code fix above

            time.sleep(2)
            pyautogui.moveTo(x=460, y=192)
        # # press and hold key
        # pyautogui.keyDown('win')
        #
        # # press  key
        # pyautogui.press('d')
        #
        # # release key
        # pyautogui.keyUp('win')

# ----------------------
# Close the webdriver
driver.quit()

# print(SchedIDNos)
# CountofSchedIDNos = len(SchedIDNos)
# mystr = str(CountofSchedIDNos)
# Prompt = "There are " + mystr + " Schedule ID Numbers"
# print(Prompt)
# PROMPT AFTER FINISHING ALL THE CODES
# create root window
root = tk.Tk()

# show info message box
mb.showinfo("I'm done Master Ayton! Boom! Panis!", Prompt)

# destroy root window
root.destroy()




