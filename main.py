import addFilm, amendFilm, delFilm, printFilms, report

menuOptions = """
1. Add a record
2. Delete a record
3. Amend a record
4. Show all records
5. Report menu
6. Exit
"""

def filmMenu():
    option = 0
    selectionList = ['1', '2', '3', '4', '5', '6']

    while option not in selectionList:
        print(menuOptions)
        selection = input("Enter selection: ")

        if selection not in selectionList:
            print(f"{selection} is not a valid option")
        return selection


def filmApplication():
    mainProgram = True
    while mainProgram:
        mainMenu = filmMenu()
        match mainMenu:
            case "1":
                addFilm.addRecord()
            case "2":
                delFilm.deleteFilm()
            case "3":
                amendFilm.amend()
            case "4":
                printFilms.printFilms()
            case "5":
                report.filmReport()
            case "6":
                input("Press Enter to close application")
                mainProgram = False


if __name__ in '__main__':
    filmApplication()