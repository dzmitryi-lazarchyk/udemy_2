def get_todos(filename='todos.txt'):
    """This function returns the list of
    todos from a read file."""
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def store_todos(todos_local, filename='todos.txt'):
    """Write the to-do items list in the text file."""
    with open(filename, 'w') as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print(get_todos())