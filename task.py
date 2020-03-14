# title: CHAPTER II
# version: 1.01
# date: 14/03/2020
# author: Marcin Grzegorz Kaspryk

import argparse
import sys
# POSTGRESQL library
import psycopg2
from datetime import date

# Fields to connect with database
DB_NAME = "noppqwsc"
DB_USER = "noppqwsc"
DB_PASS = "IEvfoWUwUJEG8PqyZDimIlaNLqVllSUM"
DB_HOST = "dumbo.db.elephantsql.com"
DB_PORT = "5432"

# Create connection to database
def connect():
    try:
        conn = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
        print("Connected to database")
        return conn
    except:
        print("Can't connect to database")

# Adds new row in TASKS table
def add_task(name, deadline, description):
    conn=connect()
    cur = conn.cursor()
    task_hash=hash(name)
    cur.execute("""
    INSERT INTO TASKS (TASK_HASH,NAME,DEADLINE,DESCRIPTION)VALUES (%s,%s,%s,%s)
    """,
    ((task_hash,name,deadline,description,))
    )
    conn.commit()
    print("Data inserted successfully")
    print("TASK_HASH: ", task_hash)
    conn.close()

# Updates row in TASKS table
def update_task(name,deadline,description,TASK_HASH):
    conn=connect()
    cur = conn.cursor()
    if name and deadline and description:
        cur.execute("""
        UPDATE TASKS SET NAME = %s, DEADLINE = %s, DESCRIPTION = %s 
        WHERE TASK_HASH = %s
        """,
        ((name,deadline,description,TASK_HASH))
        )
    elif deadline and description:
        cur.execute("""
        UPDATE TASKS SET DEADLINE = %s, DESCRIPTION = %s 
        WHERE TASK_HASH = %s
        """,
        ((deadline,description,TASK_HASH))
        )
    elif name and description:
        cur.execute("""
        UPDATE TASKS SET NAME = %s,DESCRIPTION = %s 
        WHERE TASK_HASH = %s
        """,
        ((name,description,TASK_HASH))
        )
    elif name and deadline:
        cur.execute("""
        UPDATE TASKS SET NAME = %s, DEADLINE = %s
        WHERE TASK_HASH = %s
        """,
        ((name,deadline,TASK_HASH))
        )
    elif name:
        cur.execute("""
        UPDATE TASKS SET NAME = %s 
        WHERE TASK_HASH = %s
        """,
        ((name,TASK_HASH))
        )
    elif deadline:
        cur.execute("""
        UPDATE TASKS SET DEADLINE = %s 
        WHERE TASK_HASH = %s
        """,
        ((deadline,TASK_HASH))
        )
    elif description:
        cur.execute("""
        UPDATE TASKS SET DESCRIPTION = %s 
        WHERE TASK_HASH = %s
        """,
        ((description,TASK_HASH))
        )
    conn.commit()
    print("Data updated successfully")
    conn.close()

# Removes chosen row in TASKS table
def remove_task(TASK_HASH):
    conn=connect()
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM TASKS 
        WHERE TASK_HASH = %s
        """,
        ((TASK_HASH,))
    )
    conn.commit()
    print("Data removed successfully")
    conn.close()

# Lists the tasks from table TASKS
def list_tasks(d):
    conn=connect()
    cur = conn.cursor()
    print("------------")
    if d:                                   # True --> --today
        today = date.today()
        cur.execute("""
        SELECT NAME, DEADLINE ,DESCRIPTION FROM TASKS WHERE DEADLINE = %s
        """,
        ((today,))
        )
        rows = cur.fetchall()                # fetch all selected rows
        for data in rows:
            print("name: ",data[0])
            print("deadline: ",data[1])
            print("description: ",data[2])
            print("------------")
    else:                                    # False --> --all
        cur.execute("""
        SELECT NAME, DEADLINE, DESCRIPTION FROM TASKS
        """
        )
        rows = cur.fetchall()                # fetch all selected rows
        for data in rows:
            print("name: ",data[0])
            print("deadline: ",data[1])
            print("description: ",data[2])
            print("------------")
    conn.commit()
    print("Data printed successfully")
    conn.close()

def description():     # base help if something goes wrong
    print('''
    tasks.py add --name Cleaning [--deadline DATETIME] [--description DESCRIPTION]
    tasks.py update [--name Cleaning] [--deadline DATETIME] [--description DESCRIPTION] TASK_HASH
    tasks.py remove TASK_HASH
    tasks.py list [--all | --today]
    ''')

try:
    task = sys.argv[1]  # operation name add|update|remove|list
except:
    description()

if __name__ == "__main__":
    if task == "add":
        parser = argparse.ArgumentParser()
        parser.add_argument("add", help="adds new task")
        parser.add_argument("--name",type=str, help="task name")
        parser.add_argument("--deadline",type=str, help="task deadline")
        parser.add_argument("--description",type=str, help="task description")
        args = parser.parse_args()
        if args.name is not None:
            add_task(args.name, args.deadline, args.description)
            print(args.name)
            print(args.deadline)
            print(args.description)
        else:
            print("name is required")
            description()
    elif task == "update":
        parser = argparse.ArgumentParser()
        parser.add_argument("update", help="updates task")
        parser.add_argument("--name",type=str, help="task name")
        parser.add_argument("--deadline",type=str, help="task deadline")
        parser.add_argument("--description",type=str, help="task description")
        parser.add_argument("TASK_HASH",type=int, help="task hash")
        args = parser.parse_args()
        if args.name is None and args.deadline is None and args.description is None:
            print("Nothing to update")
        else:
            update_task(args.name, args.deadline, args.description,args.TASK_HASH)
            print(args.name)
            print(args.deadline)
            print(args.description)
            print(args.TASK_HASH)
    elif task == "remove":
        parser = argparse.ArgumentParser()
        parser.add_argument("remove", help="removes task")
        parser.add_argument("TASK_HASH",type=int, help="task hash")
        args = parser.parse_args()
        remove_task(args.TASK_HASH)
        print(args.TASK_HASH)
    elif task == "list":
        size_arg = len(sys.argv)
        if size_arg > 2:
            if sys.argv[2]=="--today":
                list_tasks(1)
            else:
                list_tasks(0)
        else:
            description()
    else:
        description()
