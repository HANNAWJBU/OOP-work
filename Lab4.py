import pickle

class Customer:
    def __init__(self):
        self.cID = ""
        self.cName = ""
        self.acc_no = 0
        self.phone = 0
        self.emailID = ""
        self.bal = 0.0
        self.cCard = []
        self.dCard = []

    def add_values_to_customer(self, x):
        self.cID = x
        self.cName = input("Enter the Customer Name: ")
        self.acc_no = int(input("Enter the Account Number: "))
        self.phone = int(input("Enter the Customer's Phone Number: "))
        self.emailID = input("Enter the Customer's Email Address: ")
        self.bal = int(input("Enter the Customer's Balance: "))

    def transfer_funds(self, x):
        print("[1] Add funds to customer object")
        print("[2] Remove funds from customer object")
        opt = input("Enter your selection: ")

        if opt == "1":
            self.bal += x
        elif opt == "2":
            self.bal -= x
        else:
            print("Invalid input")

    def display_cust_info(self):
        print(self.cID)
        print(self.cName)
        print(self.acc_no)
        print(self.phone)
        print(self.emailID)
        print(self.bal)
        print(self.cCard)
        print(self.dCard)

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = 0
        self.ccv = 0
        self.exp_date = ""
        self.bal = 0

    def add_card(self, x):
        self.type = input("Enter the Card Type: ")
        self.card_no = x
        self.ccv = int(input("Enter the Card's CCV: "))
        self.exp_date = input("Enter the Card's Expiration Date: ")
        self.type = int(input("Enter the Card's Balance: "))

i = 1
ci = 1
custList = []
cardList = []

while 1:
    print("[1] Create a customer object")
    print("[2] Create a card object")
    print("[3] Transfer funds between customer objects")
    print("[4] Assign a card object to a customer object")
    print("[5] Display customer info")
    print("[6] Display card info")
    print("[7] Commit")
    print("[8] Exit")

    opt = input("Enter your selection: ")

    if opt == "1":
        cVar = "cust"+str(i)
        cVar = Customer()
        cVar.add_values_to_customer(cVar)
        custList.append(cVar)
        i+=1

    elif opt == "2":
        cardVar = "card" + str(ci)
        cardVar = Card()
        cardVar.add_card(cardVar)
        cardList.append(cardVar)
        ci += 1

    elif opt == "3":
        cust1 = input("Enter the first customer's ID")
        cust2 = input("Enter the second customer's ID")

        print("[1] Transfer from cust1 to cust2")
        print("[2] Transfer from cust2 to cust1")

        opt = input("Enter your selection")

    elif opt == "4":
        print()
    elif opt == "5":
        var = input("Enter the Customer's ID: ")

        var = Customer()
        var.display_cust_info()

    elif opt == "6":
        print()
    elif opt == "7":
        with open("customers.dat", "wb") as file1:
            pickle.dump(custList, file1)
        file1.close()

        with open("card.dat", "wb") as file2:
            pickle.dump(cardList, file2)
        file2.close()

    elif opt == "8":
        break
    else:
        print("Invalid Input")