
class Student:
    def __init__(self, name = "", usn = "", marks = []):
 # Initialize student name and USN
        self.name = name
        self.usn = usn
 # Initialize list to store marks in three subjects and total marks
        self.marks = list()
    def getMarks(self):
 # Loop to read marks for three subjects and calculate total marks
        for i in range(3):
            (self.marks).append(float(input(f"Enter marks for subject {i+1}: ")))
 
    def getdetails(self):
 # Getting the student 
        self.name = input("Enter the name: ")
        self.usn = input("Enter the USN: ")
 
    def display(self):
 # Display score card details including name, USN, marks, total marks, and p
        print("Score Card:")
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Marks in each subject:", self.marks)
        total = 0
        for x in self.marks:
            total += x
        print("Total Marks:", total)
        print("Percentage:", total/3,'%')
# Create a Student object
student1 = Student()
# Get Student Details
student1.getdetails()
# Get marks from user
student1.getMarks()
# Display score card de