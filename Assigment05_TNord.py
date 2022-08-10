# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
#           RRoot,1.1.2030, Created starter script
#           TNord,08.07.2022, Added code to complete assignment 05
#           TNord,08.08.2022, Minor code clean-up
#           TNord,08.09.2022, Added a little more user feedback to some operations
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
strFile = "ToDoList.txt"   # Data storage file
objFile = None # File Handle
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # Capture the user option selection
strTask = "" # User-entered task
strPriority = "" # User-entered priority
intDelete = "" # Capture the user option selection for delete


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

if objFile == None:
    objFile = open(strFile, "a")
    objFile.close()

objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(" | ")  # Returns a list!
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow["Task"] + " | " + dicRow["Priority"].strip())
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5]: "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if len(lstTable) == 0:
            print("There are no tasks in the list.")
        else:
            print("Task | Priority")
            for row in lstTable:
                print(row)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a Task: ")
        strPriority = input("Set a Priority: ")
        lstRow = [strTask, strPriority]
        lstTable.append(lstRow[0] + " | " + lstRow[1])
        print("\nTask added to list.")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        i = 0 # Set a variable so we can label our row numbers
        print("Task | Priority")
        for row in lstTable: # Display the current list of tasks
            i += 1 # Increment our row number
            print("(" + str(i) + ")" + " " + row) # Print our table with row numbers for easier usability
        intDelete = int(input("\nWhat row number would you like to delete? "))  # User indicates which row should be deleted
        if intDelete >= 1 and intDelete <= len(lstTable):
            del lstTable[intDelete-1] # Delete the indicated row
            if len(lstTable) == 0:
                print("\nThere are no tasks in the list.")
            else:
                print(f"\nRow {intDelete} has been deleted.\n") # Tell the user the row they selected has been deleted
                print("Task | Priority")
                for row in lstTable: # Display the new list of tasks
                    print(row)
                continue
        else:
            print("Please enter a valid number.")
            continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row + "\n")
        objFile.close()
        print(f"Tasks saved to {strFile}.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye.")
        break  # and Exit the program

    # Step 8 - Any other input, return to the menu
    else:
        continue