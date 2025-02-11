# Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Number of terms
n = int(input("Enter the number of terms: "))

# Print the Fibonacci sequence
print(f"Fibonacci sequence up to {n} terms: {fibonacci(n)}")

