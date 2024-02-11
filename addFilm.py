from connect import *

def addRecord():
    title = input("Enter the title of the film: ")
    year = int(input("Enter the release year: "))
    rating = input("Enter the age rating: ")
    duration = int(input("Enter duration in minutes: "))
    genre = input("Enter the genre: ")

    dbCursor.execute("INSERT INTO tblfilms(title, yearReleased, rating, duration, genre) VALUES(?, ?, ?, ?, ?)",(title, year, rating, duration, genre))
    dbCon.commit()

    print(f"{title} was added to the film collection!")

if __name__ == '__main__':
    addRecord()