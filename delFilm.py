from connect import *

def deleteFilm():
    IDselection = input("Enter the ID of film to delete: ")
    dbCursor.execute(f"SELECT title from tblfilms WHERE filmID = {IDselection}")
    result = dbCursor.fetchone()

    if result:
        filmTitle = result[0]
        
        dbCursor.execute(f"DELETE FROM tblfilms WHERE filmID = {IDselection}")
        dbCon.commit()

        print(f"{filmTitle} was removed from the database!")
    else:
        print(f"Film with ID {IDselection} not found in the database.")

if __name__ == '__main__':
    deleteFilm()