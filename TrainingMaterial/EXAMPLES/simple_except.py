#!/usr/bin/python3

try:
	x = 5
	y = "cheese"
	z = x + y
	print("Bottom of try")

except TypeError as e:
	print("Naughty programmer! ",e)

