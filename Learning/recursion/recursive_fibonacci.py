
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# Execution
# Output: 1, 1, 2, 3, 5, 8
n = 10
if n <= 0:
    print("Invalid input!")
else:
    print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i))

