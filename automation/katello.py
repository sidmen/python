import os
# import pyautogui
from selenium import webdriver
import time


def katello_login(username, password):
    browser = webdriver.Chrome()
    browser.get("https://katello.stsky.biz")
    username_xpath = browser.find_element_by_xpath('//*[@id="login_login"]')
    password_xpath = browser.find_element_by_xpath('//*[@id="login_password"]')
    login_xpath = browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/div/input')
    username_xpath.send_keys(username)
    password_xpath.send_keys(password)
    time.sleep(2)
    login_xpath.click()
    # pyautogui.typewrite(["enter"])
    time.sleep(1000)


login_user = os.environ.get('SSO_USERNAME')
login_password = os.environ.get('SSO_PASSWORD')
katello_login(login_user, login_password)
