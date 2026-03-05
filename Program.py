import sqlite3
from unittest import case

connection=sqlite3.connect('todo.db')
cursor=connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        todo TEXT,
        status INTEGER
    )
''')

def remove_todo():
    cursor.execute("SELECT * FROM list")
    all_tasks = cursor.fetchall()
    for task in all_tasks:
        print(task)
    rem=input('Which do you want to remove? (write index)')
    cursor.execute("DELETE FROM list where id = ?", (rem,))
    connection.commit()
    print('Done!')



print("Am schimbat si eu ceva")