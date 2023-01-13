import streamlit as st
import suck_functions

todos = suck_functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    # creates dictionary
    todos.append(todo)
    suck_functions.write_todos(todos)


st.title('My Todo App')
st.subheader('ahhhh')
st.write('dis da app')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        suck_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()  # have to rerun after checkbox

st.text_input(label='h', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')
