from datetime import datetime
import os

def check_txt_file():
    if not os.path.exists("todos.txt"):
        with open("todos.txt", "w"):
            print("create new txt file")

def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

def get_date_time():
    current_datetime = datetime.now().strftime('%d %B %Y, %H:%M:%S')
    return current_datetime

# print(get_todos())


