#!/bin/python


def read_input_fn():
    print("raw_input is for string which the input cannot be manipulated")
    print("input is for user input that can be manipulated")

    name = raw_input("What is your name? ")
    birthdate = raw_input("What is your birthdate? ")

    age = input("How old are you? ")

    print("%s was born on %s" % (name, birthdate))
    print("Half of your age is %s" % (age / 2))

read_input_fn()
