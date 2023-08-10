#PROGRAM TO FIND AREA OF TRIANGLE USING HERONS FORMULA

a=int(input("Enter length of first side : "))
b=int(input("Enter length of second side : "))
c=int(input("Enter length of thrid side : "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is :",area)