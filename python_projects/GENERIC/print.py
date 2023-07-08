print("Enter a todo: ")
###############################################
todo = input("Enter another todo: ")
print("the user entered", todo)
###############################################
user_prompt = "Enter one more todo: "
todo = input(user_prompt)
print("the user entered newly", todo)
###############################################
user_prompt_new = "Enter all todo:"
todo1 = input(user_prompt_new)
todo2 = input(user_prompt_new)
todo3 = input(user_prompt_new)

todos = [todo1, todo2, todo3, "lastItem"]
print(todos)
print(type(todo1))  # output: <class 'str'>
print(type(todos))  # output: <class 'list'>
###############################################
