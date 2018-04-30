from selenium import webdriver
# from password import *
import time
# python debugger:
import pdb
import sys


# user_name = raw_input("username: ")
# password = raw_input("password: ")
# to_list = raw_input("to: ")


###
def gmail_login(username, pwd, recipients):
    # pdb.Pdb(stdout=sys.__stdout__).set_trace()
    browser = webdriver.Chrome()
    browser.get('https://www.gmail.com')
    email_xpath= browser.find_element_by_xpath('//*[@id="identifierId"]')
    email_xpath.send_keys(username)
    next_after_email = browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
    next_after_email.click()
    time.sleep(5)
    password_xpath = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password_xpath.send_keys(pwd)
    next_after_password = browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
    next_after_password.click()
    time.sleep(10)
    compose = browser.find_element_by_xpath('//div[contains(text(),"COMPOSE")]')
    compose.click()
    time.sleep(10)
    to = browser.find_element_by_xpath('//*[@name="to"]')
    to.send_keys(recipients)
    time.sleep(5)

if __name__ == "__main__":
    gmail_login('user_name', 'password', 'to_list')
