import random
import os
import json

def receiptss():
    # pass
    dirpath = os.getcwd()
    print(dirpath)
    count = os.getenv("FILE_COUNT") or 100
    # print(count)
    words = [word.strip() for word in open('./receipts/new/words.txt').readlines()]
    # print(words)
    for identifier in range(1, count + 1): #range gives a numerable 0 to count-1 value (and it auto iterates)
        amount = random.uniform(1.0, 100.0)
        # print(amount)
        content = {
            'topic': random.choice(words),
            'value': "%.2f" % amount
            }
        with open('./receipts/new/receipt-%s.json' % identifier, 'w') as f:
            json.dump(content, f)


receiptss()
