from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import  Options

opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")

browser = webdriver.Chrome(ChromeDriverManager().install(),options=opt)

browser.get("https://t2mis.tesda.gov.ph/POAdmin/CenterScheduleEnrolls/827714")

button = browser.find_element_by_link_text("Result")
button.click()
