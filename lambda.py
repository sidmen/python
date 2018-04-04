"""
f = lambda x: 3*x + 1
print(f(2))
---is equivalent to---
def f(x):
    return 3*x + 1
print(f(2))

We CANNOT use lambda for multi line functions
"""

f = lambda x: 3*x + 1
print(f(2))


full_name = lambda f_name, l_name: f_name.strip().title() + " " + l_name.strip().title()
g = full_name("   sidharth", "MENON")
print(g)

"""
Output:
7
Sidharth Menon
"""

"""
strip() => removes whitespace
title() => capitalize each word
"""
