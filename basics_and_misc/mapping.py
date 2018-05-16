temp_in_c = [("Berlin", 29), ("Cairo", 36)]


c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

"""
above lambda function is equivalent to:

def c_to_f(x):
    return (x[0], (9/5)*x[1] + 32)
"""

temp_in_f = list(map(c_to_f, temp_in_c))
print(temp_in_f)


"""
Output:
[('Berlin', 84.2), ('Cairo', 96.8)]

here the temp is converted from C to F and is mapped

"""
