

FILEPATH = 'todos.txt'  # the constants used at multiple places


def get_todos(filepath=FILEPATH):                               # default value (if there's a non default value then that should be called before default values)
    """ Read a text file and return the list of todo items """  # this is doc-string | help(get_todos) will show this
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # this todos_local is local to the function and cannot be called outside this function.


def write_todos(todos_arg, filepath=FILEPATH):  # non-default values to be called before default values
    """ Write the todo list items to a file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return None


# help(get_todos)
# help(write_todos)

if __name__ == "__main__":
    print("you ran the myfunctions script directly")
