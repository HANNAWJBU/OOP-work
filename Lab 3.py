class Books:
    def __init__(self):
        self.Bid = "",
        self.Title = "",
        self.Authid = "",
        self.Publisher = "",
        self.Yop = 0,

    def add_book(self):
        self.Bid = input("Please insert a BookID: ")
        self.Title = input("Please insert the Book's name: ")
        self.Authid = input("Please insert the Author's ID: ")
        self.Publisher = input("Please insert the publisher's name: ")
        self.Yop = int(input("Please enter the year of publication: "))

        AddedBooks.append(self)

class Authors:
    def __init__(self):
        self.Aid = "",
        self.AName = "",
        self.Affiliation = "",
        self.Country = "",
        self.PhoneNum = 0,
        self.Email = ""
        self.AddedAuthors = []

    def add_author(self):
        self.Aid = input("Please insert a AuthorID: ")
        self.AName = input("Please insert the Author's name: ")
        self.Affiliation = input("Please insert the Author's affiliation: ")
        self.Country = input("Please insert the Author's home country: ")
        self.PhoneNum = int(input("Please enter the Author's phone number: "))
        self.Email = input("Please enter the Author's email: ")

        AddedAuthors.append(self)

class Users:
    def __init__(self):
        self.Uid = 0,
        self.UName = "",
        self.Password = "",
        self.Address = "",
        self.PhoneNum = 0,
        self.Email = "",
        self.BorrowedBooks = []

    def add_user(self):
        self.Uid = input("Please insert a UserID: "),
        self.UName = input("Please insert the User's name: ")
        self.Password = input("Please insert a new password: ")
        self.Address = input("Please insert the User's address: ")
        self.PhoneNum = input("Please enter the User's phone number: ")
        self.Email = input("Please enter the User's email: ")

        AddedUsers.append(self)

    def checkout_book(self, borrowedbook):
        print("Fired")

        self.BorrowedBooks.append(borrowedbook)
        print(self.BorrowedBooks)

    def display_borrowed_books(self):
        for x in self.BorrowedBooks:
            print("Borrowed Books: ",x.Bid, x.Title, x.AuthID, x.Publisher, x.Yop)

AddedBooks = []
AddedAuthors = []
AddedUsers = []

while 1:
    print("[1] Manage Books")
    print("[2] Manage Authors")
    print("[3] Manage Users")
    print("[4] Quit")

    opt = input("Please enter your selection: ")

    if opt == "1":
        print("Selection Received: [", opt, "]")
        print("[1] Display Books")
        print("[2] Add Books")

        opt = input("Please enter your selection: ")

        if opt == "1":
            for x in AddedBooks:
                print("Books: ",x.Bid, " : ", x.Title, " : ", x.Authid, " : ", x.Publisher, " : ", x.Yop)

        elif opt == "2":
            B1 = Books()
            B1.add_book()
        else:
            print("Invalid Selection Received")

    elif opt == "2":
        print("Selection Received: [", opt, "]")

        print("[1] Display Authors")
        print("[2] Add Authors")

        opt = input("Please enter your selection: ")

        if opt == "1":
            for x in AddedAuthors:
                print("Authors: ",x.Aid, " : ", x.AName, " : ", x.Affiliation, " : ", x.Country, " : ", x.PhoneNum, " : ", x.Email)
        elif opt == "2":
            A1 = Authors()
            A1.add_author()
        else:
            print("Invalid Selection Received")
    elif opt == "3":
        print("Selection Received: [", opt, "]")

        print("[1] Display Users")
        print("[2] Add Users")
        print("[3] Add Borrowed Books")
        print("[4] View Borrowed Books")

        opt = input("Please enter your selection: ")

        if opt == "1":
            for x in AddedUsers:
                print("Users: ", x.Uid, " : ", x.UName, " : ", x.Password, " : ", x.Address, " : ", x.PhoneNum, " : ", x.Email)
        elif opt == "2":
            U1 = Users()
            U1.add_user()

        elif opt == "3":
            User = Users()

            borrowedbook1 = input("Please insert a BookID: ")

            User.checkout_book(borrowedbook1)

        elif opt == "4":
            for x in AddedUsers:
                print("Users: ", x.Uid, " : ", x.UName, " : ", x.BorrowedBooks)
        else:
            print("Invalid Selection Received")
    elif opt == "4":
        print("Selection Received: [", opt, "]")

        break
    else:
        print("Invalid Selection Received: [", opt, "]")