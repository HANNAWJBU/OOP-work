Menu = {}

print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
print("Welcome to the Burger Shack Menu Manager!")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

tax = .92

while True:
    updateMenu = input("Would you like to load the preset menu? y/n: ")

    if updateMenu == "y":
        print("Loading preset menu!")

        itemID = "i1"
        Name = "Burger"
        Price = 7.50
        Desc = "A medium well slow cooked burger."

        Menu.update({itemID: {
            "Item": Name,
            "Price": Price,
            "Description": Desc
        }})

        itemID = "i2"
        Name = "Fries"
        Price = 3.00
        Desc = "A large bag of steak fries."

        Menu.update({itemID: {
            "Item": Name,
            "Price": Price,
            "Description": Desc
        }})

        itemID = "i3"
        Name = "Soda"
        Price = 1.50
        Desc = "A 16oz fountain drink."

        Menu.update({itemID: {
            "Item": Name,
            "Price": Price,
            "Description": Desc
        }})

        print("Displaying Current Menu!")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        for menu_items in Menu.items():
            print(menu_items)
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        print("Loading Program!")

        break

    elif updateMenu == "n":
        print("Loading Program!")
        break

    else:
        print("Invalid Command Received!")

while True:
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    print("Welcome to the Burger Shack Menu Manager!")
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

    print("[1] Process payments")
    print("[2] Change Data")
    print("[3] Add to Menu")
    print("[4] Remove from Menu")
    print("[5] View Menu")
    print("[6] Quit")

    opt = input("Please enter your selection: ")

    if opt == "1":
        print("Input Received!", "[", opt, "]")

        itemInput = input("Please enter the ID of the item Purchased: ")

        item = Menu.get(itemInput)

        paid = int(input("Please enter the amount paid: "))

        totalCost = item.Price / tax
        toReturn = paid - totalCost

        print(totalCost)
        print(toReturn)

        if toReturn < 0:
            print("Insufficient Payment Received >:(")
        elif toReturn < 0:
            print("Change: ", toReturn)
        else:
            print("Error")


    elif opt == "2":
        print("Input Received!", "[", opt, "]")
    elif opt == "3":
        print("Input Received!", "[", opt, "]")
    elif opt == "4":
        print("Input Received!", "[", opt, "]")
    elif opt == "5":
        print("Input Received!", "[", opt, "]")

        print("Displaying Menu!")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        for menu_items in Menu.items():
            print(menu_items)
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

    elif opt == "6":
        print("Input Received!", "[", opt, "]")

        print("Thank you for using the Burger Shack Menu Manager!")
        break

    else:
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        print("Invalid Input Received!", "[", opt, "]")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
