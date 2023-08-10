#PROGRAM TO FIND ROOTS OF QUADRATIC EQUATION

import math
a=float(input("Enter the coefficient of X :"))
b=float(input("Enter the coefficient of Y :"))
c=float(input("Enter the coefficient of Z :"))

d=b*b-4*a*c;
if d>0:
  r1=(-b+math.sqrt(d))/(2*a)
  r2=(-b-math.sqrt(d))/(2*a)
  print("roots are real and unequal :",r1,"and",r2)
elif d==0:
  r1=-b/(2*a)
  print("roots are real and equal :",r1)
else:
  print("roots are imaginary")
