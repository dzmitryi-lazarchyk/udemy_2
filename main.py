from functions import get_todos, store_todos
import time

print("It is " + time.strftime("%b %d, %Y %H:%M:%S %z"))

while True:
    # Get user input, remove space chars and modify it
    # to lower case.
    user_action = input("Enter show, add, edit, complete or exit: ").strip().lower()

    if user_action.startswith("add"):
        # Checking if user put todoo in command "add ..."
        if len(user_action) > 3:
            todo = user_action[4:]
        else:
            todo = input("Enter a todo: ").strip() + "\n"
        todo = todo.capitalize()

        todos = get_todos()

        todos.append(todo + "\n")

        store_todos(todos)
    elif user_action.startswith("show") or user_action.startswith("display"):
        todos = get_todos()

        for number, todo in enumerate(todos):
            print(str(number + 1) + ". " + todo.strip())
    elif user_action.startswith("edit"):
        try:
            if len(user_action) > 4:
                number = int(user_action[5:])
            else:
                number = int(input("Enter number of the todo to edit: "))
        except ValueError:
            print("Command is not valid.\n"
                  "Enter number of the task after word 'edit'.")
            continue
        index = number - 1
        todos = get_todos()

        new_todo = input(f"Enter todo you want"
                         f" to replace '{todos[index].strip()}' with:")
        todos[index] = new_todo.capitalize().strip() + "\n"

        store_todos(todos)
        print("Done!")
    elif user_action.startswith("complete"):
        try:
            if len(user_action) > 8:
                number = int(user_action[9:])
            else:
                number = int(input("Enter number of the todo that was comlited:"))
        except ValueError:
            print("Command is not valid.\n"
                  "Enter number of the task after word 'complete'.")
            continue
        index = number - 1
        todos = get_todos()

        # Message to use later in message for user about
        # successfully removed item.
        try:
            msg = f"Todo '{todos[index].strip()}' was completed!"
            todos.pop(index)
        except IndexError:
            print(f"There is no todo with number '{number}'")
            continue

        store_todos(todos)
        print(msg)
    elif user_action.startswith("exit"):
        break
    else:
        print("Unknown command.")

print('Goodbye!')
