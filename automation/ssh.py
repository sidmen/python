#!C:\Users\spoonath\AppData\Local\Programs\Python\Python36\python.exe

# CANNOT RUN THIS SCRIPT AS PXSSH IS NOT CURRENTLY SUPPORTED IN WINDOWS

import pexpect
from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()
    hostname = raw_input("hostname: ")
    username = os.environ.get('SSO_USERNAME')
    # password = getpass.getpass("password: ")
    password = os.environ.get('SSO_PASSWORD')
    cmd = raw_input("command: ")
    s.login(hostname, username, password)
    s.sendline(cmd)
    s.prompt()   # match the prompt
    print(s.before)  # print everything before the prompt
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed to login")
    print(str(e))
