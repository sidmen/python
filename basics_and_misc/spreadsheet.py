import csv

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

# csv_file = open('python_test_spreadsheet.csv')
with open('python_test_spreadsheet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # to skip the fist row since it just contains the heading of each column

    for row in csv_reader:
        name, email, accepted, coach, language = row
        # print(name, email, accepted, coach, language)

        if accepted == "yes":
            msg = ACCEPTED_MSG.format(name, coach)
        else:
            msg = REJECTED_MSG.format(name)
        print("Send email to: {}".format(email))
        print("Email content:")
        print(msg)

# csv_file.close()  # not required for "with open('filename')"
