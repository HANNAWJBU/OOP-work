name = input("Please enter your name: ")

course1 = float(input("Please enter your grade: "))
course2 = float(input("Please enter your grade: "))
course3 = float(input("Please enter your grade: "))
course4 = float(input("Please enter your grade: "))
course5 = float(input("Please enter your grade: "))

totalPoints = course1+course2+course3+course4+course5
if totalPoints > 500:
    print("Impossible total points detected")

Average = totalPoints/5

if 100 >= Average >= 90:
    print("Grade A")
elif Average >= 80:
    print("Grade B")
elif Average >= 70:
    print("Grade C")
elif Average >= 60:
    print("Grade D")
else:
    print("Grade F")
    print("(Stinky)")