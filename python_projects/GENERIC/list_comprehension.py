filenames = ["1.doc", "1.report", "1.presentation"]
new_filenames = []
for filename in filenames:
    replacement = f"{filename.replace('.', '-')}.txt"
    new_filenames.append(replacement)
print(new_filenames)

# LIST COMPREHENSION - 1 (with just one list: another_filenames)
another_filenames = ["1.doc", "1.report", "1.presentation"]
another_filenames = [f"{filename.replace('.', '-')}.txt" for filename in another_filenames]
print(another_filenames)

##################################################################3

old = [1, 2, 3]
new = []
for i in old:
    new.append(i + 10)
print(new)

# LIST COMPREHENSION - 2  (with 2 lists: old and another_new)
another_new = [i + 10 for i in old]
print(another_new)

