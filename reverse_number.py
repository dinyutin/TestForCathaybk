def reverse_numbers(numbers):
    return [int(str(num)[::-1]) for num in numbers]

numbers = [35, 46, 57, 91, 29]
reversed_numbers = reverse_numbers(numbers)
print("反轉後的數字:", reversed_numbers)
