from connect import *

def amend():
    # Get user selection for entry to modify
    IDField = input("Enter film ID to amend data (Leave field blank to skip): ")

    # Initialize lists for concatenation and value checking purposes 
    attributes = ['title', 'yearReleased', 'rating', 'duration', 'genre']
    newVals = []
    valueCheck = []

    # User inputs for data modification
    title = input("Enter updated title: ")
    year = input("Enter updated release year: ")
    rating = input("Enter updated age-rating: ")
    duration = input("Enter updated duration in minutes: ")
    genre = input("Enter updated genre: ")

    # Add values to list and initialize template for the SQL query
    newVals.extend([title, year, rating, duration, genre])
    query = f"UPDATE tblfilms SET "
    queryEnd = f" WHERE filmID = {IDField}"

    # If an input contains data it concatenates SQL syntax to the query; if blank, it adds a value to a blank field counter (valueCheck list)
    for i, value in enumerate(newVals):
        if len(value) > 0:
            # Strips single quotes as it references list items
            stripVal = "'"
            query = query + f"{attributes[i].strip(stripVal)} = {newVals[i]},"
        else:
            valueCheck.append('x')
    
    # Checks if no new data was added
    if len(valueCheck) == 5:
        print("Nothing was affected!")
    
    # Final concatenation and database commitment
    else:
        fullQuery = query[:-1] + queryEnd
        dbCursor.execute(fullQuery)
        dbCon.commit()

        print(f"Film record {IDField} was updated!")
    

if __name__ == '__main__':
    amend()