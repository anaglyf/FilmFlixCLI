import sqlite3 as sql

dbCon = sql.connect(r"Python\Week 2\D5\CLI\filmflix.db")
dbCursor = dbCon.cursor()