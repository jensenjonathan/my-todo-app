def get_todos(file_path='todos.txt'):
    """stores the values already in the file"""
    with open(file_path, 'r') as ass_file:
        ass = ass_file.readlines()
    return ass


def write_todos(cock_todos, file_path='todos.txt'):  # non-default parameter comes first
    """Writes to file. Takes list as argument"""
    with open(file_path, 'w') as ass_file:
        ass_file.writelines(cock_todos)


if __name__ == '__main__':  # only executes if suck_functions is run directly
    print('shit my nuts')
