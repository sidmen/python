#!/bin/python

"""
List: [1, 2, "a", 3.14]

List Comprehensions:
    [expr for val in collection]
    [expr for val in collection if <test>]
    [expr for val in collection if <test1> and <test2>]
    [expr for val1 in collection1 and val2 in collection2]

"""
#############################################################

squares = []
for i in range(1, 101):
    squares.append(i**2)
print(squares)

#equivalent using list comprehension:
squares2 = [i**2 for i in range(1, 101)]
print(squares2)

#############################################################

remainders = [x**2 % 5 for x in range(1, 10)]
print(remainders)


#############################################################
movies = ["star wars", "gandhi", "casablanca", "Ghostbusters"]

g_movies = []
for title in movies:
    if title.startswith('G'.lower()) or title.startswith('G'):
        g_movies.append(title)
print(g_movies)


#equivalent using list comprehension:
g_movies = [title.strip() for title in movies if title.startswith('G'.lower()) or title.startswith('G')]
print(g_movies)

#############################################################
movies_2 = [("star wars", 2000), ("gandhi", 2001), ("casablanca", 2002), ("Ghostbusters", 2003)]

post2k = [(title.strip(), year) for (title, year) in movies_2 if year > 2000 and year < 2003]
print(post2k)

#############################################################
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B ]
print('cartesian_product of A and B is %s' % cartesian_product)

#############################################################


# import argparser
#
# parser = argparser.ArgumentParser(description='Search for words including partial word')
# parser.add_argument('snippet', help='partial (or complete) string to search for in the words file')
#
# args = parser.parse_args()
# snippet = args.snippet.lower()
#
# words = open('/usr/share/dict/words').readlines()
# #################################################################
# print([word.strip() for word in words if snippet in word.lower()]) # list comprehension #word => 'keith\n', #word.strip() => 'keith'
# #################################################################
# # matches = []
# #
# # for word in words:
# #     if snippet in word.lower():
# #         matches.append(word)
# #################################################################
# print(matches)
