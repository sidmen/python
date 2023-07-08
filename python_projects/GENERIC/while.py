user_prompt = "Enter a todo:"
todos = []                           # defining an empty list to use append to it later
while True:
    todo = input(user_prompt)
    capitalTodo = todo.capitalize()  # capitalize method to be applied on the string todo
    todos.append(capitalTodo)        # append method to append todo to todos list
    print(todos)