import random

def generate_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

numbers = generate_numbers(10)
even_numbers = filter_even(numbers)
average = calculate_average(even_numbers)

print("Generated numbers:", numbers)
print("Even numbers:", even_numbers)
print("Average of even numbers:", average)