#!/bin/python

import os
#
# stage = (os.getenv("STAGE") or "development").upper() #getenv is a function
# stage = os.environ["STAGE"].upper() #environ is a dictionary
#
# output = "We're running in %s" % stage
#
# if stage.startswith("PROD"):
#     output = "DANGER!!! - " + output
#
# print(output)


if os.environ["NODE_ENV"].startswith("prod"):
    print("DANGER")

s = os.environ["PROGRAMFILES"]
print s.upper().split("\\")[0].split(" ")[0]
