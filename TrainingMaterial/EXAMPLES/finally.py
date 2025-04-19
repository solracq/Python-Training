#!/usr/bin/python3

try:
    x = 5
    y = 37
    z = x + y
    print("z is",z)
except TypeError as e:
    print("Caught exception:",e)
finally:
    print("Don't care whether we had an exception")

print()

try:
	x = 5
	y = "cheese"
	z = x + y
	print("Bottom of try")
except TypeError as e:
    print("Caught exception:",e)
finally:
	print("Still don't care whether we had an exception")

