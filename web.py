import streamlit as st
import functions
import os

if not os.path.exists("toDos.txt"):
    with open("toDos.txt", "w") as file:
        pass

todos = functions.get_toDos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To Do App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input("", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
