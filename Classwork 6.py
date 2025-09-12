myList = []

while True:
    print("Press 1 to add an element to the list.")
    print("Press 2 to remove an element to the list.")
    print("Press 3 to replace an element in the list.")
    print("Press 4 to sort the elements in the list.")
    print("Press 5 to reverse the order of the elements the list.")
    print("Press 6 display the list.")
    print("Press 7 to quit.")

    opt = int(input("Please enter your selection: "))

    if opt == 1:
        elementToAdd = input("Please enter the element you wish to add: ")
        myList.append(elementToAdd)
        print(myList)
    elif opt == 2:
        elementToRemove = input("Please enter the element you wish to remove: ")
        if myList.__contains__(elementToRemove):
            myList.remove(elementToRemove)
            print(myList)
        else:
            print("Element not found.")
    elif opt == 3:
        elementToBeReplaced = input("Please enter the element you wish to overwrite: ")
        elementToReplace = input("Please enter the new element: ")
        if myList.__contains__(elementToBeReplaced):
            myList.remove(elementToBeReplaced)
            myList.append(elementToReplace)
            print(myList)
        else:
            print("Element not found.")
    elif opt == 4:
        myList.sort()
        print(myList)
    elif opt == 5:
        myList.reverse()
        print(myList)
    elif opt == 6:
        print(myList)
    elif opt == 7:
        break
    else:
        print("Invalid input received.")
