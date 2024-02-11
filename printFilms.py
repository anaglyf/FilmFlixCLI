from connect import *

def printFilms():
    dbCursor.execute("SELECT * FROM tblfilms")

    allRecords = dbCursor.fetchall()
    for record in allRecords:
        print(record)

if __name__ == '__main__':
    printFilms()