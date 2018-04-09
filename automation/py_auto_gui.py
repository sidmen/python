import pyautogui
import time
print(pyautogui.position()) # browser address bar (268, 104)  or (280, 74) as per the video

sender = "sidharth.rulez@gmail.com"
receiver = "sidharth.rulez@gmail.com"
BODY = """
This is a sample test mail from {} to test pyautogui by python.
"""

pyautogui.click(268, 104)
pyautogui.typewrite("www.gmail.com")
pyautogui.typewrite(["enter"]) # equivalent to clicking enter
time.sleep(10)
pyautogui.click(128, 334) # compose  (128, 334) or (153, 340)
time.sleep(5)
pyautogui.click(869, 435) # to list   large:(115, 214)  small:(878, 435), (869, 435)
pyautogui.typewrite(receiver)
pyautogui.click(874, 502) # subject   large:(84, 289)  small:(874, 502)
pyautogui.typewrite("Sent using pyautogui by python")
pyautogui.click(858, 563)  # Body
pyautogui.typewrite(BODY.format(sender))
# pyautogui.click(914, 1051) # Send   large:(96, 1048) small:(914, 1051)
pyautogui.hotkey("ctrl", "enter")   # Send
