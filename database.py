import sqlite3
db= sqlite3.connect('login')
rs=db.cursor
rs.execute('''create table register (
    name varchar(40), email varachar(40), password varchar(15)''')
    