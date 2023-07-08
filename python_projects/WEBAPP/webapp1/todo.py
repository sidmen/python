import streamlit as st
import backend

st.title("My Todo App")
st.subheader("My Subheader")
st.write("This is a description")

todos = backend.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"    # st.session_state is a dict which holds the value of all the items
    todos.append(todo)
    backend.write_todos(todos)


for index, todo in enumerate(todos):
    # st.checkbox(todo)
    checkbox = st.checkbox(todo, key=todo)  # to assign a unique key to every item in the list
    if checkbox:
        todos.pop(index)
        backend.write_todos(todos)
        del st.session_state[todo]  #  to delete the todo from the session_state also
        st.experimental_rerun()     # to rerun the script immediately

st.text_input(key="new_todo",
              label="",
              placeholder="Add new todo...",
              on_change=add_todo)