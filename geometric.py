import math
n = int(input("Enter the number of elements: "))
product = 1
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    product *= num
if product < 0:
    print("Geometric mean is not defined for negative numbers.")
else:
    geometric_mean = math.pow(product, 1/n)
    print(f"The geometric mean of the numbers is: {geometric_mean:.2f}")
