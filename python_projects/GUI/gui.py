import backend
import PySimpleGUI as sg
import time

sg.theme("DarkBlue6")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",
                         key='todos_input')  # tooltip: Text that appears when mouse is hovered over the box

add_button = sg.Button(key="Add", tooltip="Add Todo", image_source="add.png", mouseover_colors="White")
edit_button = sg.Button("Edit")
complete_button = sg.Button(key="Complete", tooltip="Complete Todo", image_source="complete.png")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values=backend.get_todos(),
                      key="todos_list",
                      enable_events=True,
                      size=(45, 10)
                      )

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20)
                   )  # title of the window | in layout we used list of list, this implies the widgets in the inner list will be created on the same row

while True:
    event, values = window.read(timeout=10)     # here timeout is set to 10ms so that while loop runs every 10ms and thus the time will be refreshed automatically
    time_format = "%b %d, %Y %H:%M:%S"
    window['clock'].update(value=time.strftime(time_format))
    match event:
        case 'Add':
            todos = backend.get_todos()

            new_todos = values['todos_input'] + "\n"
            todos.append(new_todos)

            backend.write_todos(todos)

            window['todos_list'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos_list'][0]
                new_todo = values['todos_input']

                todos = backend.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                backend.write_todos(todos)

                window['todos_list'].update(values=todos)       # to refresh the list_box with updated values on the go. Note: here the parameter is "values" because it is a list
            except IndexError:
                sg.popup("Please select an item", title="Error", font=('Helvetica', 20))

        case 'Complete':
            try:
                todo_to_complete = values['todos_list'][0]
                todos = backend.get_todos()
                todos.remove(todo_to_complete)
                backend.write_todos(todos)
                window['todos_list'].update(values=todos)
                window['todos_input'].update(value="")  # to empty the input box
            except IndexError:
                sg.popup("Please select an item", title="Error", font=('Helvetica', 20))
        case 'Exit':
            exit()

        case 'todos_list':
            window['todos_input'].update(value=values['todos_list'][
                0])  # to show the selected todo in the input box. Note: here the parameter is "value" because its input box

        case sg.WIN_CLOSED:  # if window is closed
            break

window.close()
