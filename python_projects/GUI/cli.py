import backend     # from backend.py
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show or edit or complete or exit: ").strip() + "\n"

    # ADD
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = backend.get_todos()   # OR get_todos('files/NEWTODOS.txt') : to override the default value | make sure the overriden file exists
        todos.append(todo)
        backend.write_todos(todos)   # to write the contents of todos to the file | the filepath is already defined in function so no need to mention it again

    # SHOW
    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = backend.get_todos()

        for index, item in enumerate(todos):
            row = f"{index}-{item}"
            print(row.strip('\n'))

    # EDIT
    elif user_action.startswith('edit'):
        try:  # try: runs the actual program
            number = int(user_action[5:])
            todos = backend.get_todos()
            new_todo: str = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            backend.write_todos(todos)    # OR  backend.write_todos(filepath='files/todos.txt', todos_arg=todos) --> here order doesn't matter as argument name is mentioned.

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
            todos = backend.get_todos()
            todos.pop(number)
            backend.write_todos(todos)

        except IndexError:  # If the number provided is not in the range of Index
            print(f"There's no item with number {number}")

    # EXIT
    elif user_action.startswith('exit'):
        break

    else:
        print("Hey, you entered an unknown command")

print("Bye!")
