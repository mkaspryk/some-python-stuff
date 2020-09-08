# title: CHAPTER II
# version: 1.01
# date: 14/03/2020
# author: Marcin Grzegorz Kaspryk

# POSTGRESQL library
import psycopg2

# Fields to connect with database
DB_NAME = "name"
DB_USER = "user"
DB_PASS = "pass"
DB_HOST = "dumbo.db.elephantsql.com"
DB_PORT = "5432"

# Creates connection with database
try:
    conn = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)
    print("Connected to database")
except:
    print("Can't connect to database")

# Create cursor to database
cur = conn.cursor()


# Function creates table TASKS where is stored all tasks
try:
    cur.execute("""
    CREATE TABLE TASKS
    (
    TASK_HASH INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DEADLINE DATE,
    DESCRIPTION TEXT
    )
    """)
    conn.commit()
    conn.close()
    print("Created table TASKS")
except:
    print("Something goes wrong with creating database")
