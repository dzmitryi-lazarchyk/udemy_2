from functions import *
import PySimpleGUI as sg
import time

sg.theme('Black')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo")

input_box = sg.InputText(tooltip="Enter todo", size=60,
                         key="todo", default_text='')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=get_todos(), key='todos',
                      enable_events=True, size=(60, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window('My todo App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button],
                          ],
                   font=('Helvetica', 10)
                   )


while True:

    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            if values['todo']:
                todos = get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                store_todos(todos)
                input_box.update(value='')
                list_box.update(values=get_todos())
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
            except IndexError:
                sg.popup("Please, choose an item first.",
                         font=("Helvetica", 15))
                continue
            new_todo = values['todo'] + '\n'

            todos =get_todos()
            index = todos.index(todo_to_edit)
            todos[index]= new_todo
            store_todos(todos)
            list_box.update(values=todos)
            input_box.update(value='')
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
            except IndexError:
                sg.popup("Please, choose an item first.",
                         font=("Helvetica", 15))
                continue
            todos = get_todos()
            todos.remove(todo_to_complete)
            store_todos(todos)
            list_box.update(values=todos)
            input_box.update(value='')
        case 'todos':
            input_box.update(value=values['todos'][0].strip())
        case sg.WIN_CLOSED | "Exit":
            break


event = window.close()
