def factorial(n):
    # 5! = 5*4*3*2*1
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
# Execution
n = 6
if n < 0:
    print("Invalid input! Please enter a positive number")
elif n == 0:
    print("Facotiral of number 0 is 1")
else:
    print("Factorial of number", n, "is", factorial(n))
for i in range(1, n+1):
    print(factorial(i))

def recur_factorial(n, a=1):
    if n == 0:
        return a
    return recur_factorial(n-1, n*a)
# Execution
n = 6
print(recur_factorial(6))