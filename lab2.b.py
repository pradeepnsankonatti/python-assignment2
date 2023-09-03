n = int(input("Enter the value of n: "))

r = int(input("Enter the value of r: "))

# Finding factorial using functions (recursive)
def fact(n):

    if n == 0 or n == 1:
        return 1

    else:
        return n * fact(n-1)

n_minus_r = fact(n-r)

r_fact = fact(r)

print("Factorial: ", fact(n))
print("Binomial Co-efficient: ", fact(n)/(n_minus_r*r_fact))