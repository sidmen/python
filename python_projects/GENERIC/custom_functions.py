def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # this todos_local is local to the function and cannot be called outside this function.


# def write_todos(filepath, todos_arg):
def write_todos(todos_arg, filepath):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return None


while True:
    user_action = input("Type add, show or edit or complete or exit: ").strip() + "\n"

    # ADD
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos('../files/todos.txt')   # OR get_todos(filepath='files/todos.txt')

        todos.append(todo)

        write_todos(todos, '../files/todos.txt')   # to write the contents of todos to the file

    # SHOW
    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = get_todos('../files/todos.txt')

        for index, item in enumerate(todos):
            row = f"{index}-{item}"
            print(row.strip('\n'))

    # EDIT
    elif user_action.startswith('edit'):
        try:  # try: runs the actual program
            number = int(user_action[5:])

            todos = get_todos('../files/todos.txt')

            new_todo: str = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            write_todos(todos, '../files/todos.txt')    # OR  write_todos(filepath='files/todos.txt', todos_arg=todos) --> here order doesn't matter as argument name is mentioned.

        except ValueError:  # short for exception: except: to customise the output in case of error | Here ValueError comes up when the parameter pass to edit command is not an integer as per this case
            print("Command Invalid. Valid command is : edit <number>")
            continue  # continue to run the while loop | opposite of break
        except IndexError:  # If the number provided is not in the range of Index
            print(f"There's no item with number {number}")
            continue

    # COMPLETE
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos('../files/todos.txt')

            todos.pop(number)

            write_todos(todos, '../files/todos.txt')

        except IndexError:  # If the number provided is not in the range of Index
            print(f"There's no item with number {number}")

    # EXIT
    elif user_action.startswith('exit'):
        break

    else:
        print("Hey, you entered an unknown command")

print("Bye!")
