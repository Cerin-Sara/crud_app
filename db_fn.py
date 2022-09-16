import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

#database functions
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(task TEXT, task_stat TEXT, task_date DATE)')

def add_data(task,task_stat,task_date):
    c.execute('INSERT INTO tasktable(task,task_stat,task_date) VALUES(?,?,?)',(task,task_stat,task_date))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM tasktable')
    data = c.fetchall()
    return data

def view_all_task_names():
	c.execute('SELECT DISTINCT task FROM tasktable')
	data = c.fetchall()
	return data

def get_task(task):
	c.execute('SELECT * FROM tasktable WHERE task="{}"'.format(task))
	data = c.fetchall()
	return data

def get_task_by_status(task_status):
	c.execute('SELECT * FROM tasktable WHERE task_stat="{}"'.format(task_status))
	data = c.fetchall()


def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date):
	c.execute("UPDATE tasktable SET task =?,task_stat=?,task_date=? WHERE task=? and task_stat=? and task_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
	conn.commit()
	data = c.fetchall()

def delete_task(task):
    c.execute("DELETE FROM tasktable WHERE task=?",(task,))
    conn.commit()
    data = c.fetchall()
    return data