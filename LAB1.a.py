name = input("Enter the student name: ")
usn = input("Enter the student USN: ")
phy = int(input("Enter the marks obtained in Physics: "))
che = int(input("Enter the marks obtained in Chemistry: "))
mat = int(input("Enter the marks obtained in Mathematics: "))
max_marks = 300
print(30 * "*")
# Display the student details
print("Name of the Student:", name)
print("Student USN:", usn)
print(30 * "*")
# Calculate the total marks
total = phy + che + mat
print("The total marks scored by the student in Physics", phy, "Chemistry", che, "Mathematics", mat, "is", total)
print(30 * "*")
# Calculate percentage
percent = (total/max_marks) * 100
print("Percentage of the Student:", round(percent))




