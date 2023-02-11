from functions import *
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

window = sg.Window('My todo App',
                   layout=[[label, input_box, add_button],
                           [exit_button]
                          ],
                   font=('Helvetica', 10)
                   )

while True:

    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            store_todos(todos)
        case sg.WIN_CLOSED | "Exit":
            break
event = window.close()
