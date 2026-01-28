# ~~~~~~~ HELPER FUNCTIONS ~~~~~~~
def loadList():
    try:
        with open("savedList.txt", "r") as listIn:
            loadedList = listIn.readlines()
            for idx in range(len(loadedList)):
                loadedList[idx] = loadedList[idx].replace("\n", "")
        return loadedList
    except FileNotFoundError:
        return []
    


def saveList(listIn):
    with open("savedList.txt", "w") as newSave:
        for idx in range(len(listIn)):
            newSave.write(f"{listIn[idx]}\n")



def addItems(listIn):
    addMore = True
    listIn = listIn
    while addMore:
        nextItem = input("Enter item to add (or 'done' to exit) --> ").lower()
        if nextItem == "done" or nextItem == 'exit':
            addMore = False
        else:
            listIn.append(f"{nextItem}")

    saveList(listIn)

    return False



def removeItems(listIn):
    removeMore = True
    listIn = listIn
    while removeMore:
        printList(listIn)
        print("")
        toRemove = input("Select an item number to remove from the list (or 'done' to exit) --> ").lower()
        if toRemove == "done" or toRemove == 'exit':
            removeMore = False
        else:
            try:
                toRemove = int(toRemove) - 1
                listIn.pop(toRemove)
            except IndexError:
                print("Invalid item number; please select again.")

    saveList(listIn)

    return False
        


def editItems(listIn):
    editMore = True
    listIn = listIn
    while editMore:
        printList(listIn)
        print("")
        toEdit = input("Select an item number to edit (or 'done' to exit) --> ").lower()
        if toEdit == "done" or toEdit == "exit":
            editMore = False
        else:
            try:
                newEntry = input("New entry --> ")
                listIn[(int(toEdit) - 1)] = newEntry
            except IndexError:
                print("Invalid item number; please select again.")

    saveList(listIn)

    return False
    


def moveItems(listIn):
    moveMore = True
    listIn = listIn
    while moveMore:
        printList(listIn)
        print("")
        toMove = input("Select an item number to move (or 'done' to exit) --> ").lower()
        if toMove == "done" or toMove == "exit":
            moveMore = False
        else:
            try:
                oldIdx = int(toMove) - 1
                newIdx = int(input("Enter the new list position (int) --> ")) - 1
                listIn.insert(newIdx, listIn.pop(oldIdx))
            except IndexError:
                print("Invalid item number or position; please select again.")

    saveList(listIn)

    return False



def printList(listIn):
    if len(listIn) > 0:
        for idx in range(len(listIn)):
            print(f"{idx+1}. {listIn[idx]}")
    else:
        print("The list is empty.")



# ~~~~~~~ MAIN LOGIC ~~~~~~~
def main():
    appOn = True
    userList = loadList()
    while appOn:
        print("Welcome to List Manager! Choose an option:")
        print("1. Print List")
        print("2. Add Items")
        print("3. Remove Items")
        print("4. Edit Items")
        print("5. Move Items")
        print("6. Exit Application")
        userChoice = input(" --> ")

        if userChoice == "1":
            printList(userList)

        elif userChoice == "2":
            addOn = True
            while addOn:
                printList(userList)
                addOn = addItems(userList)

        elif userChoice == "3":
            removeOn = True
            while removeOn:
                removeOn = removeItems(userList)

        elif userChoice == "4":
            editOn = True
            while editOn:
                editOn = editItems(userList)

        elif userChoice == "5":
            moveOn = True
            while moveOn:
                moveOn = moveItems(userList)

        elif userChoice == "6":
            appOn = False

        else:
            print("Invalid option!")
    


# ~~~~~~~ MAIN CALL ~~~~~~~~
main()