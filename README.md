# some-python-stuff

CHAPTER I
---------------------------------
python version: python 3.7

file: CHAPTERI.py

CHAPTER II (uses database POSTGRESQL)
---------------------------------
python version: python 3.7
file: task.py
additional file: create_data_table.py (not needed)

to run project is needed postgresql:

install on Windows
pip install psycopg2

install on Linux(Ubuntu):
pip3 install psycopg2-binary

to check data in database needed is pgAdmin4
in pgAdmin panel add new server connection (Servers -> Create -> Server)

Host name/address: dumbo.db.elephantsql.com

Port: 5432

Maintenance database: noppqwsc

Username: noppqwsc

Password: IEvfoWUwUJEG8PqyZDimIlaNLqVllSUM

run script:

task.py add --name 'Cleaning' --deadline '2020-12-23' --description 'Cleaning home for Christmas' 

task.py update --name 'Running' --deadline '29-12-2020' --description 'For health' 2434143532

task.py remove 2434143532

task.py list --all

CHAPTER III
---------------------------------
![alt text](https://raw.githubusercontent.com/mkaspryk/some-python-stuff/branch/images/to/password.png)
