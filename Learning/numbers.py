import random
import math

def months(lista: list):
    if len(lista) > 1:
        print("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}".format(*lista))
    else:
        print("{0}".format(lista))
    print("My bMonth is: {7}".format(*lista))
    num = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eight",
           "ninth", "tenth", "eleventh", "twelveth"]
    for i in range(0, len(lista)):
        print(f"{i} {num[i]} - {lista[i]}")
    print("\n{0[7]} - {1[7]}".format(num, lista))

def random_gen():
    rand = random.randint(0, 50)
    print(f"Random number generated from 1 - 50: {rand}")
    print(f"Random w/ range : {random.randrange(0, 100, 10)}")

def multiplication(a, b):
    result = 0
    ap = 0
    bp = 0
    if isinstance(a, int) and isinstance(b, int):
        if a != 0 and b != 0:
            if a < 0 or b < 0:
                ap = abs(a)
                bp = abs(b)
            else:
                ap = a
                bp = b
            for i in range(bp):
                result += ap
        else:
            result = 0
    else:
        raise Exception("Input numbers must be integers")
    if a < 0 and b > 0:
        return f"-{result}"
    if a > 0 and b < 0:
        return f"-{result}"
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return result

def division(a, b):
    mod = 0
    dividend = abs(a)
    divisor = abs(b)
    count = 0
    if divisor != 0:
        while dividend >= divisor:
            mod = dividend - divisor
            dividend = mod
            count += 1
    else:
        return f"Divisor {b} must not be zero or alpha char"
    return f"{count} with mod = {mod}"

def div(a, b):
    res = 0
    count = 0
    if b == 0:
        return "No zero division!"
    if a > b:
        res = a - b
        count = 1
        while res >= 1:
            res -= b
            count += 1
    return count
print(div(9, 3))

def mod(a, b):
    dividend = abs(a)
    divisor = abs(b)
    return abs(divisor * (dividend // divisor) - dividend)

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a ^ b, (a & b) << 1)

def substract(a, b):
    if b == 0:
        return a
    else:
        return substract(a ^ b, (~a & b) << 1)

def factorial(num):
    res = 1
    while num >= 1:
        res *= num
        num -= 1
    return res

def recursive_factorial(num):
    if num <= 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)

def recursive_fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return recursive_fibonacci(num-1) + recursive_fibonacci(num-2)

def printmatrix(size:int):
    if size >= 4:
        for i in range(1, size + 1):
            print(random.randint(0, 90), end=" ")
            if i % 4 == 0:
                print()
    else:
        print("input a matrix size bigger than 4")

def compare(a, b):
    if a ^ b == 0:
        print(f"{a} == {b}")
    else:
        print(f"{a} != {b}")

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400:
                leap = True
    return leap

def get_mod(a, b):
    # 7 / 2 = 3  mod = 1
    # formula : 2*3 - 7 =1
    # a = dividend = 7
    # b = divisor = 2
    result = a - (b * (a // b))
    assert result == a % b, "wrong result!"
    return result

# convert from dec to bin
def dec_bin(num):
    res = num
    lista = []
    while res >= 2:
        mod = res % 2
        lista.append(str(mod))
        res = res // 2
    lista.append(str(res))
    lista.reverse()
    return "".join(lista)

def dec_bin_recursive(num):
    if num == 0:
        return ""
    else:
        return dec_bin_recursive(num // 2) + str(num % 2)

num = 6
print(num)
print(dec_bin(num))
print(dec_bin_recursive(num))

# convert from bin to dec
def bin_dec(bnum):
    lista = list(bnum)
    lista.reverse()
    result = 0
    for i in range(len(lista)):
        result += int(lista[i]) * 2 ** i
    return result

print(bin_dec(dec_bin_recursive(num)))

# convert from dec to hex
def toHex(dec):
    x = (dec % 16)
    digits = "0123456789ABCDEF"
    rest = dec / 16
    if (rest == 0):
        return digits[int(x)]
    return toHex(rest) + digits[int(x)]

print(hex(num))
print(toHex(6))

if __name__ == "__main__":
    lista = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    months(lista)

    random_gen()
    a = -3
    b = -2
    print(f"{a} X {b} = {multiplication(a, b)}")

    a = 7
    b = 2
    print(f"{a} / {b} = {division(a, b)}")

    print(f"{a} mod {b} = {mod(a, b)}")

    print(f"{a} + {b} = {sum(a, b)}")

    print(f"{a} - {b} = {substract(a, b)}")

    # factorial 3! = 3 * 2 * 1
    num = 20
    print(f"{num}! = {factorial(num)}")
    print(f"{num}! = {recursive_factorial(num)}")
    print(f"Fibonacci of {num} = {recursive_fibonacci(num)}")

    printmatrix(16)

    compare(2,3)
    compare(3,3)

    year = 2003
    print(is_leap(year))
    print("\n")

    import math
    array = [(43, 6571), (22, 8294), (62, 3628), (88,4773), (56, 2829), (89, 4340), (75, 8195), (29, 4872), (63, 1890), (31, 6263), (96, 5379), (48, 7246)]
    for numbers in array:
        a, b = numbers
        print(f"{b} / {a} = {math.trunc(b/a)} R{get_mod(b, a)}")

