class Students:
    def __init__(self):
        self.Sid = "",
        self.Name = "",
        self.Major = "",
        self.Dob = "",
        self.CreditHours = 0.0,
        self.GPA = 0.0,
        self.courses = []

    def add_student(self):
       self.Sid = input("Enter the Sid: ")
       self.Name = input("Enter the Name: ")
       self.Major = input("Enter the Major: ")
       self.Dob = input("Enter the Dob: ")
       self.CreditHours = float(input("Enter the Credit Hours: "))
       self.GPA = float(input("Enter the GPA: "))

    def edit_student(self):
        self.Sid = input("Enter the Sid: ")
        self.Name = input("Enter the Name: ")
        self.Major = input("Enter the Major: ")
        self.Dob = input("Enter the Dob: ")
        self.CreditHours = float(input("Enter the Credit Hours: "))
        self.GPA = float(input("Enter the GPA: "))

    def display_student(self):
        print("Student ID: ", self.Sid)
        print("Name: ", self.Name)
        print("Major: ", self.Major)
        print("Dob: ", self.Dob)
        print("Credit Hours: ", self.CreditHours)
        print("GPA: ", self.GPA)

        for x in self.courses:
            print("Courses: ", x.Cname)

    def register_course(self, cc1):
        self.courses.append(cc1)

class Courses:
    def __init__(self):
        self.Cid = "",
        self.Cname = "",

    def add_course(self):
        self.Cid = input("Please enter the Cid: ")
        self.Cname = input("Please enter the course name: ")

s1 = Students()

s1.add_student()

s2 = Students()
s3 = Students()

s1.display_student()


c1 = Courses()
c2 = Courses()

c1.add_course()
c2.add_course()

s1.register_course(input("Enter the Cid: "))
s1.register_course(input("Enter the Cid: "))

s1.display_student()