import math

Menu = {}

print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
print("Welcome to the Burger Shack Menu Manager!")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

tax = .08

def printMenu():
    for menu_items in Menu.items():
        print(menu_items)
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

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
        print("")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

        printMenu()

        print("")
        print("Loading Program!")

        break

    elif updateMenu == "n":
        print("Loading Program!")
        break

    else:
        print("Invalid Command Received!")

while True:
    print("")
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    print("Welcome to the Burger Shack Menu Manager!")
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    print("")

    print("[1] Process payments")
    print("[2] Change Data")
    print("[3] Add Items to Menu")
    print("[4] Remove Items from Menu")
    print("[5] View Menu")
    print("[6] Quit")

    opt = input("Please enter your selection: ")

    if opt == "1":
        print("Input Received!", "[", opt, "]")

        printMenu()

        itemInput = input("Please enter the ID of the item Purchased: ")
        item = Menu[itemInput]
        itemPrice = item["Price"]
        totalCost = itemPrice * (1 + tax)
        cost = math.floor(totalCost * 100) / 100

        print("Item Price: ", cost)

        paid = float(input("Please enter the amount paid: "))
        toReturn = paid - cost


        change = math.ceil(toReturn * 100) / 100

        print("Amount Paid: ", paid, " - ", "Item Price: ", cost, " = ", change)

        if toReturn > 0:
            print("Change: ", change)

        elif toReturn == 0:
            print("No Change")

        elif toReturn < 0:
            print("Insufficient Payment Received >:(")

        else:
            print("Error")

    elif opt == "2":
        print("Input Received!", "[", opt, "]")
        print("Current Tax: ", 100 * tax, "%")
        opt = input("Change Tax Rate? y/n: ")

        while 1:
            if opt == "y":
                tax = float(input("Please enter the new tax percentage: "))

                if tax < 1:
                    print("Current Tax: ", 100 * tax, "%")
                elif tax > 1:
                    print("Current Tax: ", tax, "%")
                    newTax = tax/100

                    tax = newTax
                elif tax == 1:
                    print("Current Tax: ", 100 * tax, "%")
                else:
                    print("Invalid Tax")
                break

            elif opt == "n":
                print("Returning to menu")
                break

            else:
                print("Invalid input")

    elif opt == "3":
        print("Input Received!", "[", opt, "]")

        printMenu()

        iID = input("Enter a new ItemID: ")
        name = input("Enter the Item's name: ")
        price = float(input("Enter the Item's price: "))
        desc = input("Enter the Item's description: ")

        Menu.update({iID: {
            "Name":name,
            "Price":price,
            "Desc":desc
        }})

        print("Item Added!")

    elif opt == "4":
        print("Input Received!", "[", opt, "]")
        printMenu()

        toRemove = input("Enter the ID of the Item you wish to remove: ")
        del Menu[toRemove]
        print("Item Removed!")

    elif opt == "5":
        print("Input Received!", "[", opt, "]")

        print("Displaying Menu!")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

        printMenu()

    elif opt == "6":
        print("Input Received!", "[", opt, "]")
        print("Thank you for using the Burger Shack Menu Manager!")
        break

    else:
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        print("Invalid Input Received!", "[", opt, "]")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
