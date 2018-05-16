#!/bin/python

def gather_info():
    height = float(raw_input("What is your height? (inches or meters): "))
    weight = float(raw_input("What is your weight? (pounds or kilograms): "))
    unit = raw_input("Are your measurements in metric or imperial units?: ").lower().strip()
    return (height, weight, unit) #use tuple to return multiple items

def calculate_bmi(weight, height, unit='metric'):
    if unit.startswith('m'):
        bmi = 703 * (weight / (height ** 2))
    else:
        bmi = (weight / (height ** 2))
    print ("Your BMI is %s" % bmi)

while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(height=height, weight=weight, unit='imperial')
        break #else it will go into infinite loop
    elif unit.startswith('m'):
        calculate_bmi(weight, height)
        break #else it will go into infinite loop
    else:
        print("Error: Unknown measurement system. Please use imperial or metric")
