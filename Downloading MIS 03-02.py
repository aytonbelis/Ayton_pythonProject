from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import re
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

# Set the path to the Microsoft Edge webdriver
service = EdgeService(executable_path="C:\Program Files\msedgedriver.exe")

# Create an instance of the Edge class using the service
# driver = webdriver.Edge(service=service)

#press and hold Ctrl key
pyautogui.keyDown('win')

#press  key
pyautogui.press('2')

#release Ctrl key
pyautogui.keyUp('win')

# #search bar
# pyautogui.moveTo(x=400, y=65)
# pyautogui.click()
#
# pyautogui.typewrite("https://t2mis.tesda.gov.ph/NewReport/Terminal?sked=414764")
# pyautogui.press('enter')

# # Navigate to the website
# driver.get("https://t2mis.tesda.gov.ph/NewReport/Terminal?sked=414764")
#
# #input email
# email_field = driver.find_element_by_name("Email")
# email_field.send_keys("etdoniego@tesda.gov.ph")
#
# #input password
# password_field = driver.find_element_by_name("Password")
# password_field.send_keys("7fraters")
#
# #locate and press login button
# login_button = driver.find_element_by_xpath("//input[@type='submit']")
# login_button.click()
#
# # Wait for the page to load
# driver.implicitly_wait(3)

#locate the save button
#save_button = driver.find_element_by_id('ReportViewer_ctl05_ctl04_ctl00_ButtonImg')
#save_button.click()


#------------------------------------
#press and hold Ctrl key
#pyautogui.keyDown('ctrl')
#
# #press J key
# pyautogui.press('j')
#
# #release Ctrl key
# pyautogui.keyUp('ctrl')
#
# #move mouse pointer to open elipsis download settings
# pyautogui.moveTo(x=1118, y=131)
# pyautogui.click()
# #download settings
# pyautogui.moveTo(x=844, y=256)
# pyautogui.click()
# #enable, 1070 x dati, 483
# pyautogui.moveTo(x=1070, y=683)
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()
#back to original page
#pyautogui.moveTo(x=230, y=45)
#pyautogui.click()
#-----------------------------------------------

#move mouse pointer to the Save Button image
pyautogui.moveTo(x=557, y=248)
# #left click image
pyautogui.click()
#
# #move mouse pointer to the Excel option
pyautogui.moveTo(x=607, y=311)
# #left click image
pyautogui.leftClick()

# #save as
pyautogui.moveTo(x=1557, y=200)

import time
time.sleep(1)

pyautogui.leftClick()

pyautogui.press('backspace')
ayton = "12345"

pyautogui.typewrite(ayton)
time.sleep(1)
pyautogui.press('enter')


