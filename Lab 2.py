myEmployees = {}

while True:
    print("Welcome to the employee manager!")
    print("--------------------------")
    print("Input [1] to add an employee to the system.")
    print("Input [2] to remove an employee to the system.")
    print("Input [3] to modify an employee in the system.")
    print("Input [4] to display all employees.")
    print("Input [5] to exit.")
    print("--------------------------")

    selection = input("Please enter your selection: ")

    if selection == "1":
        print("Selection received! ", "[", selection, "]")

        eID = input("Please enter a new employee ID: ")
        name = input("Please enter the employee's Name: ")
        bPay = int(input("Please enter the employee's new BasicPay: "))
        allow = int(input("Please enter the employee's new Allowance: "))
        dduct = int(input("Please enter the employee's new Deductions: "))
        taxes = int(input("Please enter the employee's new Taxes: "))

        nPay = bPay + allow
        gPay = dduct + taxes

        myEmployees.update({eID: {
            "Name": name,
            "BasicPay":bPay,
            "Allowance":allow,
            "Deductions":dduct,
            "Taxes":taxes,
            "NetPay":nPay,
            "GrossPay":gPay
        }})

    elif selection == "2":
        print("Selection received! ", "[",selection,"]")

        for employee_record in myEmployees.items():
            print(employee_record)
            print("-------------------------")

        toDel = input("Please select an employee to delete: ")
        del myEmployees[toDel]

        for employee_record in myEmployees.items():
            print(employee_record)
            print("-------------------------")

    elif selection == "3":
        print("Selection received! ", "[",selection,"]")

        for employee_record in myEmployees.items():
            print(employee_record)
            print("-------------------------")

        eID = input("Please enter the ID you would like to overwrite: ")
        name = input("Please enter the employee's Name: ")
        bPay = int(input("Please enter the employee's new BasicPay: "))
        allow = int(input("Please enter the employee's new Allowance: "))
        dduct = int(input("Please enter the employee's new Deductions: "))
        taxes = int(input("Please enter the employee's new Taxes: "))

        nPay = bPay+allow
        gPay = dduct+taxes

        myEmployees.update({eID: {
            "Name": name,
            "BasicPay": bPay,
            "Allowance": allow,
            "Deductions": dduct,
            "Taxes": taxes,
            "NetPay": nPay,
            "GrossPay": gPay
        }})

    elif selection == "4":
        print("Selection received! ", "[",selection,"]")
        print("Displaying all employees.")

        for employee_record in myEmployees.items():
            print(employee_record)
            print("-------------------------")

    elif selection == "5":
        print("Selection received! ", "[",selection,"]")
        print("Thank you for using the employee manager!")
        break
    else:
        print("Invalid selection received! ", "[",selection,"]")