Range = int(input("Find prime numbers upto you want : "))

print("\nAll prime numbers upto", Range, "are : ")

for num in range(2, Range + 1):

    i = 2

    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;
    if(i != num):
        print(num, end=" ")
