def find_odd_numbers(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    return odd_numbers
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = find_odd_numbers(my_array)

print("Odd numbers in the array:", odd_numbers)
