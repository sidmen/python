# todos = []     # commented this because we define it in the case add to read the contents of the file and assign it to todos variable

while True:
    user_action = input("Type add, show or edit or complete or exit: ").strip()  # strip method to remove whitespace in the user's input

    match user_action:
        case 'add':
            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()           # no need to close the file while using "with" context manager

            todo = input("Enter a todo: ") + "\n"  # breakline to print list content in different lines in text file
            todos.append(todo)

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)             # no need to close the file while using "with" context manager

        case 'show' | 'display':  # OR operator
            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()          # no need to close the file while using "with" context manager

            for index, item in enumerate(todos):  # enumerate function extracts the index of the element in the list and also the element itself
                # print(index, '-', item)         # output: 0 - someitem   (no control on the whitespace)
                row = f"{index}-{item}"           # f-strings: to control the format of the output
                print(row)                        # output: 0-someitem    (whitespace controlled)

        case 'edit':
            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()

            number: int = int(input("Number of the todo to edit starting with 0: "))  # int() is required because value of input is str.
            new_todo: str = input("Enter new todo: ")    # here str represents a hint for the developer to the type of the variable
            todos[number] = new_todo                     # assigns value of new_todo to the indexed number of todos list

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Number of the todo to complete: "))
            todos.pop(number)  # pop() function is to remove the element at the index from the list | you can also use remove() function but you have to specify the element itself instead of index

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break
        case _:  # a variable defined on the fly and need not be used anywhere | case x or case whatever or case _ all are same |  this any case should be at the last, because any case under this will not be reachable
            print("Hey, you entered an unknown command")

print("Bye!")
