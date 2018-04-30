import pyautogui
import time


print(pyautogui.position())  # browser address bar (268, 104)  or (280, 74) as per the video

sender = "sidharth.rulez@gmail.com"
receiver = "sidharth.rulez@gmail.com"
subject_of_email = "Sent using pyautogui by python"

BODY = """ This is a sample test mail from {} to test pyautogui by python. """


def open_gmail():
    pyautogui.click(268, 104)  # normal:(268, 104) selenium:(301, 143)
    pyautogui.typewrite("www.gmail.com")
    pyautogui.typewrite(["enter"])  # equivalent to clicking enter
    time.sleep(10)


def compose():
    pyautogui.click(128, 334)  # compose  (128, 334) or (153, 340)
    time.sleep(5)


def receiver_list(to):
    pyautogui.click(869, 435)  # to list   large:(115, 214)  small:(878, 435), (869, 435)
    pyautogui.typewrite(receiver)
    pyautogui.typewrite(["enter"])
    time.sleep(5)


def subject(subj):
    pyautogui.click(869, 500)  # subject   large:(84, 289)  small:(874, 502)
    pyautogui.typewrite(subj)
    time.sleep(2)


def body(body_of_email):
    pyautogui.click(858, 563)  # Body
    pyautogui.typewrite(body_of_email)
    time.sleep(2)


def send():
    # pyautogui.click(914, 1051) # Send   large:(96, 1048) small:(914, 1051)
    pyautogui.hotkey("ctrl", "enter")   # Send


open_gmail()
compose()
receiver_list(receiver)
subject(subject_of_email)
body(BODY.format(sender))
send()
