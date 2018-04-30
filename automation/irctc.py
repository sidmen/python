import pyautogui
import time

import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def open_irctc():
    pyautogui.click(268, 104)  # normal:(268, 104) selenium:(301, 143)
    pyautogui.typewrite("www.irctc.co.in")
    pyautogui.typewrite(["enter"]) # equivalent to clicking enter
    time.sleep(5)

def irctc_login(username, password):
    pyautogui.typewrite(username)
    pyautogui.hotkey("tab")
    pyautogui.typewrite(password)


def waitfor(myxpath, sec, element):
     try:
         myobj=WebDriverWait(driver,sec).until(EC.presence_of_element_located((By.XPATH,myxpath)))
         return myobj
     except:
         print(element)

def logindetails(USERNAME, PASSWORD):
        driver=webdriver.Chrome()
        driver.get('https://www.irctc.co.in/eticketing/loginHome.jsf')
        eleuserid='//*[@id="usernameId"]'
        elepassword='//*[@id="loginFormId"]/div[1]/div[2]/table[1]/tbody/tr[2]/td[2]/input'
        elecap='//*[@id="nlpAnswer"]'
        user=waitfor(eleuserid,10,'user field problem')
        user.send_keys(USERNAME)
        passw=waitfor(elepassword,10,'pass field problem')
        passw.send_keys(PASSWORD)
        captch=waitfor(elecap,10,'cap')
        captch.clear()
        try:
            WebDriverWait(driver,5).until(EC.alert_is_present())
            alert =driver.switch_to_alert()
            alert.accept()
            loginstatus()
        except:
            loginstatus()

# open_irctc()
logindetails("sidsta", "spq718")
