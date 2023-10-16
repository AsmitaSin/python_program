n = int(input("Enter the number of terms for the Fibonacci series: "))

a, b = 0, 1

print(a, end=' ')
print(b, end=' ')

for _ in range(2, n):
    c = a + b
    print(c, end=' ')
    a, b = b, c
