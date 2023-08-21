import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)

sl.title("My Todo App \U0001F4DD")
sl.subheader("List of To-doS: ")


for index,todo in enumerate(todos):
    check_state = sl.checkbox(todo, key=todo)
    if check_state:
        print(index,check_state)
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()        #rerun script

sl.text_input(label="", placeholder="Add a new todo",
              key="new_todo",
              on_change=add_todo)

# ###---for ref---###
# print("hello")
# # sl.session_stat





