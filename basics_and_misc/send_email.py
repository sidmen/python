import csv
import smtplib
from password import *

# python debugger:
import pdb
import sys

ACCEPTED_MSG = """
Hi {},

We are thrilled to let you know that you are accepted to our programming workshopself.

Your coach is {}.

Thank you,
Organizers
"""

REJECTED_MSG = """
Hi {},

We are very sorry to let you know that due to a big number of applications
we couldn't fit you at the workshop this time.

Thank you,
Organizers
"""
pdb.Pdb(stdout=sys.__stdout__).set_trace()
# csv_file = open('python_test_spreadsheet.csv')
with open('python_test_spreadsheet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # to skip the fist row since it just contains the heading of each column

    #set the gmail smtp server
    smtp = smtplib.SMTP('smtp.gmail.com')
    # The below 3 lines starting and ending with ehlo is used to encrypt our creds during transmission
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)

    for row in csv_reader:
        name, email, accepted, coach, language = row
        # print(name, email, accepted, coach, language)

        if accepted == "yes":
            msg = ACCEPTED_MSG.format(name, coach)
        else:
            msg = REJECTED_MSG.format(name)
        # print("Send email to: {}".format(email))
        # print("Email content:")
        # print(msg)
        #
        print(SENDER_EMAIL, email, msg)
        smtp.sendmail(SENDER_EMAIL, email, msg)

    smtp.quit()

# csv_file.close()  # not required for "with open('filename')"
