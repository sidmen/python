import pyautogui
from selenium import webdriver
import time


def vcenter_login(username, password):
    browser = webdriver.Chrome()
    browser.get('https://vcenter.corvisa.it')
    username_xpath = browser.find_element_by_xpath('//*[@id = "username"]')
    username_xpath.send_keys(username)
    # time.sleep(2)
    password_xpath = browser.find_element_by_xpath('//*[@id="password"]')
    password_xpath.send_keys(password)
    # time.sleep(2)
    pyautogui.typewrite(["enter"])
    time.sleep(1000)


vcenter_login('admin.spoonath@corvisa.com', 'moped-2NA/Xp')
