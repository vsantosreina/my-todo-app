FILEPATH = "toDos.txt"
def get_toDos(filepath=FILEPATH):
    """Read a text file and return the list of  to-do items"""
    with open(filepath, 'r') as file_local:
        toDos_local = file_local.readlines()
    return toDos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)