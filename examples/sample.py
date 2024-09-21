def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number > limit:
            break
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

limit = 100
fibonacci_numbers = generate_fibonacci(limit)
print(fibonacci_numbers)