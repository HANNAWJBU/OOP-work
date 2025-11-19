import math
import pickle

Menu = {}
Cart = []

class User:
    def __init__(self):
        self.Cid = ""
        self.PaymentType = ""
        self.Member = ""

    def add_values(self):
        self.Cid = input("Please enter a unique Customer ID: ")
        self.PaymentType = input("Enter Chosen Payment Type: ")
        self.Member = input("Membership Status: ")

class Admin:
    def __init__(self):
        self.Aid = ""
        self.Name = ""
        self.Password = ""

    def add_values(self):
        self.Aid = input("Please enter a unique Admin ID: ")
        self.Name = input("Please enter the Admin's Name: ")
        self.Password = input("Please enter a new Password: ")

    def save(self):
        with open("admin.dat", "ab") as file1:
            pickle.dump(self, file1)
        file1.close()

print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
print("Welcome to the Burger Shack Menu Manager!")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

tax = .08
global loggedIn
loggedIn = False

def login(x):
    aID = input("Please enter your Admin ID: ")
    Password = input("Please enter your Admin Password: ")
    f2 = open("admin.dat", "rb")
    working = False

    while 1:
        try:
            data = pickle.load(f2)

            if aID == data.Aid and Password == data.Password:
                working = True
                x = True
                loggedIn = x
                return x


        except EOFError:
            break

    if working:
        print("Logging In As: ", data.Name)
        print(loggedIn)

    else:
        print("Incorrect Login Credentials")

def print_menu():
    for menu_items in Menu.items():
        print(menu_items)
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

def add_to_cart():
    Var = input("Please enter the ID of the item selected: ")

    itemAdd = Menu[Var]
    Cart.append(itemAdd)

    print(Cart)

def remove_from_cart():
    Var = input("Please enter the ID of the item you wish to remove: ")

    itemAdd = Menu[Var]
    Cart.remove(itemAdd)

    print(Cart)

def process_purchase():
    total = 0
    print(Cart)

    for Var in Cart:
        total += Var["Price"]

    PostTaxTotal = total*(1+tax)

    print("The Total Is: ", PostTaxTotal)
    paid = float(input("Please enter the amount paid: "))
    toReturn = paid - PostTaxTotal
    print("Amount Paid: ", paid, " - ", "Item Price: ", PostTaxTotal, " = ", toReturn)

    if toReturn > 0:
        calculationmoney = toReturn * 100
        fifty_dollar = 5000
        twenty_dollar = 2000
        ten_dollar = 1000
        five_dollar = 500
        one_dollar = 100
        quarter = 25
        dime = 10
        nickle = 5
        penny = 1
        amount = 0

        while calculationmoney >= fifty_dollar:
            calculationmoney -= fifty_dollar
            amount += 1
        print("x", amount, "$50 bill due.")
        amount = 0
        while calculationmoney >= twenty_dollar:
            calculationmoney -= twenty_dollar
            amount += 1
        print("x", amount, "$20 bill due.")
        amount = 0
        while calculationmoney >= ten_dollar:
            calculationmoney -= ten_dollar
            amount += 1
        print("x", amount, "$10 bill due.")
        amount = 0
        while calculationmoney >= five_dollar:
            calculationmoney -= five_dollar
            amount += 1
        print("x", amount, "$5 bill due.")
        amount = 0
        while calculationmoney >= one_dollar:
            calculationmoney -= one_dollar
            amount += 1
        print("x", amount, "$1 bill due.")
        amount = 0
        while calculationmoney >= quarter:
            calculationmoney -= quarter
            amount += 1
        print("x", amount, "Quarter due.")
        amount = 0
        while calculationmoney >= dime:
            calculationmoney -= dime
            amount += 1
        print("x", amount, "Dime due.")
        amount = 0
        while calculationmoney >= nickle:
            calculationmoney -= nickle
            amount += 1
        print("x", amount, "Nickle due.")
        amount = 0
        while calculationmoney >= penny:
            calculationmoney -= penny
            amount += 1
        print("x", amount, "Penny due.")

    elif 0 == toReturn:
        print("No Change")

    elif toReturn < 0:
        print("Insufficient Payment Received >:(")

    else:
        print("Error")

def save_menu():
    with open("menu.txt", "wb") as file1:
        pickle.dump(Menu, file1)
    file1.close()

#Menu Loader
while 1:
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

        print_menu()

        print("")
        print("Loading Program!")

        break

    elif updateMenu == "n":
        print("Loading Program!")
        break

    else:
        print("Invalid Command Received!")

#Login Loop
while 1:
    if loggedIn == False:
        print("Would you like to login?")
        opt = input("y/n: ")

        if opt == "y":
            adminVar = Admin()
            loggedIn = login(False)
            break
        elif opt == "n":
            break
        else:
            print("Error")
    else:
        break

#Main Loop
while 1:
    #Check if user is admin or customer
    if loggedIn == False:
        print("[1] Proceed To Checkout")
        print("[2] View Menu")
        print("[3] Add Items To Cart")
        print("[4] View / Remove Items From Cart")
        print("[Q] Quit")

    elif loggedIn == True:
        print("[1] Proceed To Checkout")
        print("[2] View Menu")
        print("[3] Add Items To Cart")
        print("[4] Remove Items from Menu")
        print("[5] Modify Menu Items")
        print("[6] Change Data")
        print("[7] Save Menu File")
        print("[8] Add Items to Menu")
        print("[9] View / Remove Items From Cart")
        print("[10] Manage Users")
        print("[Q] Quit")

    opt = input("Please enter your selection: ")

    if opt == "1":
        print("Input Received!", "[", opt, "]")

        process_purchase()

    elif opt == "2":
        print("Input Received!", "[", opt, "]")

        print("Displaying Menu!")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

        print_menu()

    elif opt == "3":
        add_to_cart()

    elif opt == "4":
        print(Cart)
        print("[1] Remove Items")
        print("[2] Quit")
        opt = input("Enter your selection: ")

        while 1:
            if opt == "1":
                remove_from_cart()
            elif opt == "2":
                break
            else:
                print("Invalid Selection Received")

    elif opt == "5":
        print("Input Received!", "[", opt, "]")

        print_menu()

        iID = input("Enter the ItemID: ")
        name = input("Enter the Item's new name: ")
        price = float(input("Enter the Item's new price: "))
        desc = input("Enter the Item's new description: ")

        Menu.update({iID: {
            "Name": name,
            "Price": price,
            "Desc": desc
        }})

        print("Item Modified!")

    elif opt == "6":
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
                break

    elif opt == "7":
        print("Saving Menu!")
        save_menu()
        print("Saved Successfully!")

    elif opt == "8":
        print("Input Received!", "[", opt, "]")

        print_menu()

        iID = input("Enter a new ItemID: ")
        name = input("Enter the Item's name: ")
        price = float(input("Enter the Item's price: "))
        desc = input("Enter the Item's description: ")

        Menu.update({iID: {
            "Name": name,
            "Price": price,
            "Desc": desc
        }})

        print("Item Added!")

    elif opt == "9":
        print("Input Received!", "[", opt, "]")
        print_menu()

        toRemove = input("Enter the ID of the Item you wish to remove: ")
        del Menu[toRemove]
        print("Item Removed!")

    elif opt == "10":
        while 1:
            print("[1] Add New Admin User")
            print("[2] Add New Customer")
            print("[3] Delete Customer")
            print("[4] Quit")

            opt = input("Enter your selection: ")

            if opt == "1":
                adminVar = Admin()
                adminVar.add_values()
                adminVar.save()

            elif opt == "2":
                userVar = User()
                userVar.add_values()

            elif opt == "3":
                userVar = User()
                userVar.__delattr__("Cid")
                userVar.__delattr__("PaymentType")
                userVar.__delattr__("Member")

            elif opt == "4":
                break

            else:
                print("Error")

    elif opt == "Q":
        print("Input Received!", "[", opt, "]")
        print("Thank you for using the Burger Shack Menu Manager!")
        break

    else:
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        print("Invalid Input Received!", "[", opt, "]")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")