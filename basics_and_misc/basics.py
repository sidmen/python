#!bin/python

# def datatypes(type):
#     if type = "string":
#         print "'string'"
#     else
#         print "nothing"
#
#
# datatypes(string)

#################################################################
#                          FUNCTIONS                            #
#################################################################


def calc(i):
    # i = '2'
    print "int value = " + str(int(i)*4-1)
    print "float value = " + str(float(i)*4-1)

def findfn(word, letter):
    s = word.lower().find(letter)
    print "letter " + letter + " found at position " + str(s) + " in the word " + word.lower()

def stringfn(word1, word2):
    a = "Words " + word1 + " and " + word2 + " concatenated to " + word1 + word2
    b = (word1 + " ") * 4
    c = word1.lower()
    d = word2.upper()
    print a
    print b
    print c + d

def booleanfn():
    print "Booleans are 'True' & 'False'. Nothingness is 'None'"
    print "To print boolean of something 'bool('something')'"

def listfn(element1, element2, element3, element4, element5, element6, element7, element8):
    my_list = [element1, element2, element3, element4, element5, element6]
    new_list = [element7, element8]
    print "length of list is " + str(len(my_list))
    print "my_list is " + str(my_list)
    print "element2 of my_list is " + str(my_list[1])
    print "last element of my_list is " + str(my_list[-1])
    print "element2 to element5 are " + str(my_list[1:5])
    print "adding steps to alternate " + str(my_list[1:5:2])
    print "you can change the element in the list by my_list[2] = 'new value'"
    print "append the list by my_list.append('new_value') or 'my_list + new_list' for " + str(my_list + new_list)
    print "to remove some elements from the list 'my_list[1:3] = []' or 'my_list.remove(element4)' or 'my_list.pop(element4)'"
    print "to remove the last element 'new_list.pop()'"

def tuplefn(item1, item2):
    my_tuple = (item1, item2)
    print "my_tuple = " + str(my_tuple)
    print "my name is %s %s" % my_tuple

def dictfn():
    print "Dictionary order is not guarenteed"
    # my_dict = {key1: value1, key2: value2, key3: value3}
    my_dict = {'sid': 27, 'ash': 26, 'ammu': 24}
    print "my_dict = " + str(my_dict)
    print "Sid age is " + str(my_dict['sid'])
    print "to add more items to Dictionary 'my_dict['sesha'] = 27'"
    print "to remove item from Dictionary 'del my_dict['sid']' or 'my_dict.pop('sid')'"
    print "to get values 'my_dict.values()'"
    print "to get keys 'my_dict.keys()'"
    print "to get the items 'my_dict.items()'" + str(my_dict.items())
    print "to convert items into Dictionary 'new_dict = dict(my_dict.items())' " + str(dict(my_dict.items()))


def conditionalfn(my_item):
    item = 'this'
    if item == my_item:
        print "my_item is equal to item"
    else:
        print "my_item is NOT equal to item"

    if len(item) == len(my_item):
        print "length is same"
    elif len(item) >= len(my_item):
        print "item length is MORE than my_item"
    elif len(item) <= len(my_item):
        print "item length is LESS than my_item"
    else:
        print "cannot compute"


def whileloopfn():
    print "Loops in python are 'while loop' and 'for loop'"
    count = 0
    while count < 10:
        print("we are counting")
        count += 1

def forloopfn():
    print "Loops in python are 'while loop' and 'for loop'"
    colors = ['blue', 'green', 'red', 'purple']
    for color in colors:
        print(color)
    loop_dict = {'sid': 27, 'ash': 26, 'ammu': 24}
    for key, value in loop_dict.items():
        print(key)
        print(value)

def logicfn():
    if not len("something") > 10:
        print("it's not")
    a = 10
    b = 1.0
    if a is 10:
        print("true")
    if a and b:
        print(a and b)
    if a or b:
        print(a or b) #prints value of a since a is truthy and it stops there
#################################################################
#                          IMPLEMENTATION                       #
#################################################################

# calc(2.4)

# findfn('douBle', 'b')

# stringfn('sid', 'sta')

# booleanfn()

# listfn(1, 2, 3, 4, 5, 6, 7, 8)

# tuplefn('sid', 'men')

# dictfn()

# conditionalfn('thats')

# whileloopfn()

# forloopfn()

logicfn()
