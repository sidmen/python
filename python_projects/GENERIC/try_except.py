
while True:
    user_action = input("Type add, show or edit or complete or exit: ").strip() + "\n"

    # ADD
    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('../files/todos.txt', 'w') as file:
            file.writelines(todos)

    # SHOW
    elif user_action.startswith('show') or user_action.startswith('display'):
        with open('../files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index}-{item}"
            print(row.strip('\n'))

    # EDIT
    elif user_action.startswith('edit'):
        try:                                            # try: runs the actual program
            number = int(user_action[5:])

            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo: str = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:                              # short for exception: except: to customise the output in case of error | Here ValueError comes up when the parameter pass to edit command is not an integer as per this case
            print("Command Invalid. Valid command is : edit <number>")
            continue                # continue to run the while loop | opposite of break

    # COMPLETE
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            with open('../files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(number)

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:                  # If the number provided is not in the range of Index
            print(f"There's no item with number {number}")

    # EXIT
    elif user_action.startswith('exit'):
        break

    else:
        print("Hey, you entered an unknown command")

print("Bye!")
