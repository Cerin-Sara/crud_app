import streamlit as st
import pandas as pd
from db_fn import *
import plotly_express as px
st.title("Todo App")

menu =["Create","Read","Update","Delete"]
def sidebar():
    with st.sidebar:
        choice = st.radio("MENU",menu)
        return choice
choice = sidebar()

create_table()
if choice == "Create":
    st.subheader("Add items") 
    col1,col2= st.columns(2) 
    with col1:
        task =st.text_area("Task To Do")
    with col2:
        status=["To Do","Doing","Done"]
        task_stat=st.selectbox("Task Status",status)
        task_date=st.date_input("Task Date")
    if st.button('Create task'):
        add_data(task,task_stat,task_date)
        st.write("Created {task} with status {task_stat} and date {task_date}".format(task=task,task_stat=task_stat,task_date=task_date))
    


elif choice == "Read":
    st.subheader("View Items")
    result = view_all_data()
    df = pd.DataFrame(result,columns=['Task','Status','Date'])
    with st.expander("View Data"):
        st.dataframe(df)
    with st.expander("Task Status"):
        task_df = df['Status'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        fig = px.pie(task_df,values='Status',names='index')
        st.plotly_chart(fig)


elif choice == "Update":
		st.subheader("Edit Items")
		with st.expander("Current Data"):
			result = view_all_data()
			clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
			st.dataframe(clean_df)

		list_of_tasks = [i[0] for i in view_all_task_names()]
		selected_task = st.selectbox("Task",list_of_tasks)
		task_result = get_task(selected_task)
    
		if task_result:
			task = task_result[0][0]
			task_status = task_result[0][1]
			task_due_date = task_result[0][2]

			col1,col2 = st.columns(2)
			
			with col1:
				new_task = st.text_area("Task To Do",task)
			with col2:
				new_task_status = st.selectbox(task_status,["ToDo","Doing","Done"])
				new_task_due_date = st.date_input(task_due_date)

			if st.button("Update Task"):
				edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
				st.success("Updated ::{} ::To {}".format(task,new_task))

			with st.expander("View Updated Data"):
				result = view_all_data()
				clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
				st.dataframe(clean_df)

elif choice == "Delete":
    st.subheader("Delete items")
    result = view_all_data()
    df = pd.DataFrame(result,columns=['Task','Status','Date'])
    with st.expander("View Data"):
        st.dataframe(df)
    list_of_tasks = [i[0] for i in view_all_task_names()]
    selected_task = st.selectbox("Task to Delete",list_of_tasks)
    st.warning("You are about to delete {}".format(selected_task))
    if st.button("Delete Task"):
        delete_task(selected_task)
        st.write("Deleted {}".format(selected_task))
    result = view_all_data()
    df = pd.DataFrame(result,columns=['Task','Status','Date'])
    with st.expander("View Data"):
        st.dataframe(df)

else:
    st.subheader("ABOUT")