import sqlite3
from unittest import case



def remove_todo():
    cursor.execute("SELECT * FROM list")
    all_tasks = cursor.fetchall()
    for task in all_tasks:
        print(task)
    rem=input('Which do you want to remove? (write index)')
    cursor.execute("DELETE FROM list where id = ?", (rem,))
    connection.commit()
    print('Done!')

def mark_done():
    cursor.execute("SELECT * FROM list")
    all_tasks = cursor.fetchall()
    for task in all_tasks:
        print(task)
    done_id=input('Which do you want to mark done? (write index)')
    cursor.execute("UPDATE list set stastus = ? where id = ?", ("Done!",done_id,))
    connection.commit()

def show_todos():
    print('Do you want to see all todos?')
    print('1. for all todos')
    print('2. for pending todos')
    print('3. for done todos')
    decision=input('What do you want to do?')
    if decision=='1':
     cursor.execute("SELECT * FROM list")
     all_tasks = cursor.fetchall()
     for task in all_tasks:
         print(task)
    elif decision=='2':
        cursor.execute("SELECT * FROM list where status = ?", ('Pending',))
        pending_tasks = cursor.fetchall()
        for task in pending_tasks:
            print(task)
    elif decision=='3':
        cursor.execute("SELECT * FROM list where status = ?", ('Done!',))
        done_tasks = cursor.fetchall()
        for task in done_tasks:
            print(task)
while True:
 print('---- To do list ----')
 print('1). List todos.')
 print('2). Add to do task.')
 print('3). Delete a to do task.')
 print('4). Change status.')
 print('5). Exit')
 decision=input('What do you want to do?')
 match decision:
     case '1': show_todos()
     case '2': add_todo()
     case '3': remove_todo()
     case '4': mark_done()
     case '5':
            print('Bye!')
            break
     case _:
         print('Invalid input')
connection.close()

print("Am schimbat si eu ceva")