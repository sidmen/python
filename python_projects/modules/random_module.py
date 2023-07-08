import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

number = random.randint(lower_bound, upper_bound)    # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)
# OR -  number = random.randrange(lower_bound, upper_bound + 1)
print(number)