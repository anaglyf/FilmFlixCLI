from connect import *

def printRecs():
    records = dbCursor.fetchall()
    for record in records:
        print(record)

def filmReport():
    repLoop = True
    while repLoop:
        menuText = "\n1. Print details of all films \n2. Print films from a specific year \n3. Print films with a specific rating \n4. Print films of a specific genre \n5. Search for film \n6. Exit report menu\n"
        print(menuText)

        selection = int(input("Enter selection: "))
        selection -= 1

        fieldList = ['', 'yearReleased', 'rating', 'genre']
        printList = ['', 'year', 'age rating', 'genre']

        selectAll = "SELECT * FROM tblfilms "
        
        if selection == 0:
            dbCursor.execute(selectAll)
            printRecs()
        elif selection < 4:
            attribute = input(f"Enter {printList[selection]} value to check: ")
            query = selectAll + f"WHERE {fieldList[selection]} = ?"
            dbCursor.execute(query, (attribute.capitalize(),))
            printRecs()
        elif selection == 4:
            searchTerm = input(f"Search for film title: ")
            query = selectAll + f"WHERE title LIKE '%{searchTerm}%'"
            dbCursor.execute(query)
            printRecs()
        elif selection == 5:
            repLoop = False
        else:
            print("Invalid selection. Try again")


if __name__ == '__main__':
    filmReport()