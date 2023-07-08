meals = ['pasta', 'pizza', 'salad']
word = "python"
names = ["sidharth menon", "revathy rajan", "vihaan sidharth"]

for meal in meals:
    print(meal.capitalize())     # prints each item of meals list, capitalized

for letter in word:
    print(letter.capitalize())   # prints each letter of "python", capitalized

for name in names:
    print(name.title())          # prints each item of names list, with first letters of each word capitalized

print("Bye!")


