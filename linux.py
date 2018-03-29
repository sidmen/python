import os
import glob
import shutil
import json

def linux():
    try:
        os.mkdir("./processed")
    except OSError as err:
        print(err)
        print("'processed' directory already exists")

        # Get a list of receipts
        receipts = glob.glob('./receipts/new/receipt-[0-9]*.json')
        print(receipts)
        # Iterate over the receipts
        #     read content and tally a subtotal
        #     mv the file to the processed directory
        #     print that we processed the file
        subtotal = 0.0
        for path in receipts:
            with open(path) as f:
                content = json.load(f)
                subtotal += float(content['value']) # the variable value is defined in the receipts-%s.json file
                name = path.split('\\')[-1]
                destination = "./processed/%s" % name
                shutil.move(path, destination)
                print("moved '%s' to '%s'" % (path, destination))

                #Print the subtotal of all processed receipts
                print("Receipts subtotal: %.2f" % subtotal)
