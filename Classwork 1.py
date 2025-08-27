print("Super fancy wage calculator")

name = input("Hello employee, please enter your name: ")

wages = int(input("Enter hourly wage: "))
hours = int(input("Enter the amount of hours you worked: "))
days = int(input("Enter the of days you worked: "))

totalMoney = wages*hours*days



print(name, ",", "You made: ", totalMoney,"$ this month!")