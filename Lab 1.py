while 1:
    print("Welcome to my application!")
    print("---------------------------")
    print("Input 1 for Addition.")
    print("Input 2 for Subtraction.")
    print("Input 3 for Multiplication.")
    print("Input 4 for Division.")
    print("Input 5 to quit the application.")
    print("---------------------------")

    option = input("Please enter your choice: ")
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))

    if option == "1":
        print(num1, " + ", num2, " = ", num1+num2)
    elif option == "2":
        print(num1, " - ", num2, " = ", num1-num2)
    elif option == "3":
        print(num1, " * ", num2, " = ", num1*num2)
    elif option == "4":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            print(num1, " / ", num2, " = ", num1 / num2)
    elif option == "5":
        print("Thank you for using my application")
        break
    else:
        print("Invalid input received.")