import streamlit as st
# app title
st.title('📒 TO DO List App')
#installation session state:
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
# sidebar Heading
st.sidebar.header('📌 Mange Your Task')

# text input
new_task = st.sidebar.text_input('Enter Your Task:', placeholder='Enter Your Task Here.....')

if st.sidebar.button('Add Task'):
    if new_task.strip():
        st.session_state.tasks.append({'task': new_task, 'completed': False})
        st.success('**** Task Added Successfully!. ****')
    else:
        st.warning('**** Task can not be empty ****')
# display task
st.subheader('📝 Your TO_DO List')
if not st.session_state.tasks:
    st.info('***** No Task Found yet add some task from sidebar *****')
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7,0.15,0.15])

        # mark task as completed
        completed = col1.checkbox(f'{task["task"]}', task['completed'], key=f'checkbox_{index}')
        if completed != task['completed']:
            st.session_state.tasks[index]['completed'] = completed

        # update task
        if col2.button('edit', key=f'edit_{index}'):
            new_task = st.text_input('Edit Task:', task['task'], key=f'edit_input_{index}')
            if new_task and st.button('save', key=f'save_{index}'):
                st.session_state.tasks[index]['task'] = new_task
                st.experimental_rerun()

        # delete task
        if col3.button('delete', key=f'delete_{index}'):
            st.session_state.tasks(index)
            st.experimental_rerun()
    # clear all task 
    if st.button("clear all tasks"):
        st.session_state.tasks = []
        st.success('***** All Task Cleared Successfully *****')

        # footer
        st.markdown('...')
        st.caption('**** You are Always connected with simple TO_DO List App. ****')