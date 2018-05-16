import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1 ]
avg = statistics.mean(data)

print(avg)

filtered_values = list(filter(lambda x: x > avg, data))
print(filtered_values)
"""
above lambda function is equivalent to:

def filtered_values(y):
    


"""



"""
Output:
2.183333333333333
[2.7, 4.1, 4.3]

i.e., avg and the values above avg

"""
