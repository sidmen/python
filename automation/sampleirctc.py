import time
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


########## Login Details #############
USERNAME="sidsta"
PASSWORD="spq718"
######################################

######### Train Details ##############
TRAINNO="12728"
FROM="SECUNDERABAD JN - SC"
TO="ANAKAPALLE - AKP"
DOJ="16-09-2017"
CLASS="SL" # 1A EC 2A FC 3A 3E CC SL - Only these are Supported
QUOTA="GN" # [ GN=GENERAL ] [ PT=PREMIUM TATKAL ] [ HP=PHYSICALLY HANDICAP ]
           # [ LD=LADIES ] [ TQ=TATKAL ]
#####################################

######## Passengers Details #########
NAME='Kumar Raja' # Max Character 16
AGE='21'
GENDER='M' # [ M=Male F=Female ]
BERTH="LB" # [ LB=LOWER ] [ MB=MIDDLE ] [ UB=UPPER ] [ SL=SIDE LOWER ] [ SU=SIDE UPPER ]
####################################

######## Card Details ##############
CARDNUMBER='121231231212'
EXP_MONTH='4' # 1 2 3 4 5 6 7 8 9 10 11 12
EXP_YEAR='2017'
CARDNAME='Kumar Raja'
ATMPIN='1234' # Only 4 Digits
###################################

driver=webdriver.Chrome()
def mainfunction():
    def waitfor(myxpath,sec,element):
        try:
            myobj=WebDriverWait(driver,sec).until(EC.presence_of_element_located((By.XPATH,myxpath)))
            return myobj
        except:
            print(element)
    def logindetails():
        driver.get('https://www.irctc.co.in/eticketing/loginHome.jsf')
        eleuserid='//*[@id="usernameId"]'
        elepassword='//*[@id="loginFormId"]/div[1]/div[2]/table[1]/tbody/tr[2]/td[2]/input'
        elecap='//*[@id="captchaImg"]'
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
    global filldata
    def filldata():
        lstatus.click()
        train=waitfor('//*[@id="qbform:trainNUmber"]',10,'Train Field')
        train.send_keys(TRAINNO)
        froms=waitfor('//*[@id="qbform:fromStation"]',10,'From Field')
        froms.send_keys(FROM)
        tos=waitfor('//*[@id="qbform:toStation"]',10,'To Field')
        tos.send_keys(TO)
        doj=waitfor('//*[@id="qbform:qbJrnyDateInputDate"]',10,'Date of Journey Field')
        doj.send_keys(DOJ)
        classtype=waitfor('.//option[@value="' + CLASS + '"]',10,'Class Field')
        classtype.click()
        quota=waitfor('.//option[@value="' + QUOTA + '"]',10,'Qutoa Field')
        quota.click()
        submit=waitfor('.//*[@id="qbform:quickBookSubmit"]',10,'Submit Field')
        submit.click()
        fillingstatus()
    global passengerdetails
    def passengerdetails():
        passenger.send_keys(NAME)
        Age=waitfor('//input[contains(@id,"addPassengerForm:psdetail:0:")][@class="input-style1 psgn-age only-numeric"]',10,'Age Field')
        Age.send_keys(AGE)
        Gender=waitfor('.//select[@id="addPassengerForm:psdetail:0:psgnGender"]/option[@value="M"]',10,'Gender Field')
        Gender.click()
        eleBerth='.//*[@id="addPassengerForm:psdetail:0:berthChoice"]/option[@value="' + BERTH + '"]'
        Berth=waitfor(eleBerth,10,'Berth Field')
        Berth.click()
        AutoUpgrade=waitfor('.//*[@id="addPassengerForm:autoUpgrade"]',10,'Auto Upgrade')
        AutoUpgrade.click()
        SecondCap=waitfor('.//*[@id="nlpAnswer"]',10,'Captcha Field')
        TRType=waitfor('//*[@id="DEBIT_CARD"]/label',10,'Debit Card')
        TRType.click()
        Bank=waitfor('//td[text()="HDFC Bank"]/input[@id="DEBIT_CARD"]',10,'Bank Field')
        Bank.click()
        SecondCap.clear()
        passengerstatus()

    def  makepayment():
        CardNumber=waitfor('.//*[@id="Ecom_Payment_Card_Number_Debit"]',10,'Card Number Error')
        CardNumber.send_keys(CARDNUMBER)
        Exp_Month=waitfor('.//*[@id="Ecom_Payment_Card_ExpDate_Month_Debit"]/option[@value="' + EXP_MONTH + '"]',10,'Expiry Month Field')
        Exp_Month.click()
        Exp_Year=waitfor('.//*[@id="Ecom_Payment_Card_ExpDate_Year_Debit"]/option[@value="' + EXP_YEAR + '"]',10,'Expiry Year Field')
        Exp_Year.click()
        CardName=waitfor('.//*[@id="Ecom_Payment_Card_Name_Debit"]',10,'CardName Field')
        CardName.send_keys(CARDNAME)
        AtmPin=waitfor('.//*[@id="normalPinID"]',10,'CardName Field')
        PCaptch=waitfor('//*[@name="Ecom_Captcha_Value"]',10,'Captch Field')
        PCaptch.clear()
    global loginstatus
    def loginstatus():
        try:
            global lstatus
            lstatus=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="quickbookTab:header:inactive"]/span')))
            print("Login Successfull")
            filldata()
        except:
            logindetails()
    global fillingstatus
    def fillingstatus():
        try:
            global passenger
            passenger=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[contains(@id,"addPassengerForm:psdetail:0:")][@class="input-style1 psgn-name"]')))
            print("Filling Succesful")
            passengerdetails()
        except:
            home=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="topnav"]/li[8]/ul/li[3]/a')))
            home.click()
            filldata()
    def passengerstatus():
        try:
            pstatus=WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Ecom_Payment_Card_Number_Debit"]')))
            print("Passenger Filling Successfull")
            makepayment()
        except:
            print("Something Wrong Filling Again")
            passengerdetails()

    logindetails()
mainfunction()
