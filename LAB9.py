
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
 
    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return Complex(real_part, imag_part)
 
    def __str__(self):
        return f"{self.real} + {self.imag}i"
# Create two Complex objects
ca = Complex(-2, -5)
cb = Complex(12, 8)
# Display the calculation and result
print(ca, '+', cb, '=', (ca + cb))
# Display the type and memory address of ca
print('\n',type(ca), id(ca), '\n')
# Create an empty list to store Complex numbers
complex_list = []
# Read the number of Complex numbers to add
n = int(input("How many complex numbers you want to add:"))
# Loop to input and store the Complex numbers
for i in range(n):
    r = float(input("Enter the real part of the complex number: "))
    im = float(input("Enter the imaginary part of the complex number:"))
    print()
    complex_list.append(Complex(r, im))
# Initialize a Complex object to hold the sum
sum_series = Complex()
# Loop to calculate the sum of Complex numbers in the list
for j in complex_list:
    sum_series += j
 
# Display the sum of the Complex numbers
print("\nThe sum of the given Complex numbers is:", sum_series)