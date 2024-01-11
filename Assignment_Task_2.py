"""
Task 2: Generate Fibonacci Series
Problem Statement:
Write a Python program that generates the Fibonacci sequence up to a specified number of
terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the
sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the
user to enter the number of terms (n) they want in the sequence and then display the
Fibonacci sequence up to that number of terms
"""

def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for i in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generating the Fibonacci sequence
fib_sequence = generate_fibonacci(num_terms)

print("Fibonacci sequence up to", num_terms, "terms:")
print(fib_sequence)
