Start = 100
End = 200
for num in range(Start,End+1):
    sum_of_digit = sum(int(digit)for digit in str(num))
    if sum_of_digit % 2 == 0: 
        print(num)


