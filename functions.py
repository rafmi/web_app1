FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    """Read txt file and return list of to-do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath = FILEPATH):
    """Write the to-do items list in text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_local)

