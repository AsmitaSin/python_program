#program for reverse a given number
number = int(input("Enter a integer value:: "))
rev = 0
#while(number > 0):
if number > 0:
    dig = number % 10
    rev = (rev*10)+number % 10
    number = number//10
    print("Reverse of a given integer:: ",rev)
