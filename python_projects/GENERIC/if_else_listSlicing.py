# todos = []     # commented this because we define it in the case add to read the contents of the file and assign it to todos variable

while True:
    user_action = input("Type add, show or edit or complete or exit: ").strip() + "\n"  # strip method to remove whitespace in the user's input

    # if 'add' in user_action:                   # Eg: user_action = 'add Play Chess' | "in" and "not in" are used | Bug: it will become True even if add is anywhere in the line
    if user_action.startswith('add'):           # to make sure its True only if add is at the start, but not anywhere else
        todo = user_action[4:]                 # List Slicing [4:] => 4th letter to last | Eg: user_action = 'add Play Chess' | todo = 'Play Chess'

        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()           # no need to close the file while using "with" context manager

        todos.append(todo)

        with open('../files/todos.txt', 'w') as file:
            file.writelines(todos)             # no need to close the file while using "with" context manager

    # elif 'show' in user_action or 'display' in user_action:   # Boolean operator "or" in conjunction with if condition
    elif user_action.startswith('show') or user_action.startswith('display'): # Bug: it will become True even if show is anywhere in the line
        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()          # no need to close the file while using "with" context manager

        for index, item in enumerate(todos):  # enumerate function extracts the index of the element in the list and also the element itself
            # print(index, '-', item)         # output: 0 - someitem   (no control on the whitespace)
            row = f"{index}-{item}"           # f-strings: to control the format of the output
            print(row.strip('\n'))            # output: 0-someitem    (whitespace controlled)

    # elif 'edit' in user_action:             # Bug: it will become True even if edit is anywhere in the line
    elif user_action.startswith('edit'):                 # Eg: user_action = 'edit Play Chess'
        number = int(user_action[5:])

        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo: str = input("Enter new todo: ") + "\n"   # here str represents a hint for the developer to the type of the variable
        todos[number] = new_todo                           # assigns value of new_todo to the indexed number of todos list

        with open('../files/todos.txt', 'w') as file:
            file.writelines(todos)

    # elif 'complete' in user_action:
    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number)  # pop() function is to remove the element at the index from the list | you can also use remove() function but you have to specify the element itself instead of index

        with open('../files/todos.txt', 'w') as file:
            file.writelines(todos)

    # elif 'exit' in user_action:
    elif user_action.startswith('exit'):
        break

    else:  # a variable defined on the fly and need not be used anywhere | case x or case whatever or case _ all are same |  this any case should be at the last, because any case under this will not be reachable
        print("Hey, you entered an unknown command")

print("Bye!")
