file = open('members.txt', 'r')
members = file.readlines()
file.close()

new_member = input("Add a new member: ")
members.append(new_member + "\n")
print(members)

file = open('members.txt', 'w')
file.writelines(members)
file.close()