todos = []

while True:
    user_action = input("Type add, show or edit or complete or exit: ").strip()  # strip method to remove whitespace in the user's input

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':                  # OR operator
            # for item in todos:                  # FOR LOOP
            #     print(item)
            for index, item in enumerate(todos):  # enumerate function extracts the index of the element in the list and also the element itself
                # print(index, '-', item)         # output: 0 - someitem   (no control on the whitespace)
                row = f"{index}-{item}"           # f-strings: to control the format of the output
                print(row)                        # output: 0-someitem    (whitespace controlled)
        case 'edit':
            number: int = int(input("Number of the todo to edit starting with 0: "))    # int() is required because value of input is str.
            new_todo: str = input("Enter new todo: ")   # here str represents a hint for the developer to the type of the variable
            todos[number] = new_todo                    # assigns value of new_todo to the indexed number of todos list
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number)                      # pop() function is to remove the element at the index from the list | you can also use remove() function but you have to specify the element itself instead of index
        case 'exit':
            break
        case _:      # a variable defined on the fly and need not be used anywhere | case x or case whatever or case _ all are same |  this any case should be at the last, because any case under this will not be reachable
            print("Hey, you entered an unknown command")

print("Bye!")
