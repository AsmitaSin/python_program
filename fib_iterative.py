#fibnocci series using iterative method
num = int(input("Enter the number of terms for the Fibonacci series: "))

a, b = 0, 1

print(a, end=' ')
print(b, end=' ')

for i in range(0, num):
    if i <= 1:
        print(i)
    else:
        Fib = a+b
        a = b
        b = fib
    print(fib)
